from fastapi import FastAPI, UploadFile, File, Form, Body
from fastapi.responses import FileResponse

from services.pdf_service import (
    save_uploaded_file,
    extract_text_from_pdf
)

from services.topic_service import (
    find_topic_content
)

from services.llm_service import (
    generate_presentation,
    regenerate_presentation
)

from services.pptgen_service import (
    generate_pptx
)

app = FastAPI()
CURRENT_SLIDES = None
CURRENT_TOPIC = None


@app.get("/")
def home():

    return {
        "message": "PPT LLM Backend Running Successfully"
    }
@app.post("/generate-slides")
async def generate_slides(
    file: UploadFile = File(...),
    topic: str = Form(...)
):

    try:

        file_path = save_uploaded_file(file)

        pdf_text = extract_text_from_pdf(file_path)

        relevant_content = find_topic_content(
            pdf_text,
            topic
        )

        if not relevant_content.strip():

            relevant_content = pdf_text[:1000]

        slides_data = generate_presentation(
            topic,
            relevant_content
        )
        global CURRENT_SLIDES
        global CURRENT_TOPIC

        CURRENT_SLIDES = slides_data
        CURRENT_TOPIC = topic

        return {
            "status": "review_required",
            "topic": topic,
            "slides": slides_data
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }
@app.post("/regenerate-slides")
async def regenerate_slides(
    payload: dict = Body(...)
):

    try:

        topic = payload.get("topic", "")

        feedback = payload.get("feedback", "")

        current_slides = payload.get(
            "slides",
            {}
        )

        slides_data = regenerate_presentation(
            topic=topic,
            content="",
            current_slides=current_slides,
            feedback=feedback
        )
        global CURRENT_SLIDES
        global CURRENT_TOPIC

        CURRENT_SLIDES = slides_data
        CURRENT_TOPIC = topic

        return {
            "status": "review_required",
            "topic": topic,
            "slides": slides_data
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }



@app.post("/generate-ppt")
async def generate_ppt():

    global CURRENT_SLIDES

    try:

        if CURRENT_SLIDES is None:

            return {
                "status": "error",
                "message": "No slides generated yet"
            }

        ppt_path = generate_pptx(
            CURRENT_SLIDES
        )

        return {
            "status": "success",
            "ppt_file": ppt_path
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