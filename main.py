from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse

from services.pdf_service import (
    save_uploaded_file,
    extract_text_from_pdf
)

from services.topic_service import (
    find_topic_content
)

from services.llm_service import (
    generate_presentation
)

from services.pptgen_service import (
    generate_pptx
)

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "PPT LLM Backend Running Successfully"
    }


@app.post("/generate-ppt")
async def generate_ppt(
    file: UploadFile = File(...),
    topic: str = Form(...)
):

    try:

        # Save PDF
        file_path = save_uploaded_file(file)

        # Extract PDF Text
        pdf_text = extract_text_from_pdf(file_path)

        # Find Topic Content
        relevant_content = find_topic_content(
            pdf_text,
            topic
        )

        # Fallback
        if not relevant_content.strip():

            relevant_content = pdf_text[:1000]

        # Generate Slides JSON using Ollama
        slides_data = generate_presentation(
            topic,
            relevant_content
        )

        # Generate PPT using PptxGenJS
        ppt_path = generate_pptx(
            slides_data
        )

        return {
            "status": "success",
            "topic": topic,
            "ppt_file": ppt_path,
            "slides": slides_data
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }


@app.get("/download-ppt")
def download_ppt():

    return FileResponse(
        path="output/generated_presentation.pptx",
        filename="generated_presentation.pptx",
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation"
    )