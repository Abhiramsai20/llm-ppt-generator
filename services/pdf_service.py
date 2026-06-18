import os
import fitz


def save_uploaded_file(file, upload_dir="uploads"):
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_path


def extract_text_from_pdf(pdf_path):
    text = ""

    pdf_document = fitz.open(pdf_path)

    for page in pdf_document:
        text += page.get_text()

    pdf_document.close()

    return text