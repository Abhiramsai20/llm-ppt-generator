# LLM PPT Generator

An AI-powered PowerPoint Presentation Generator that creates PPT presentations from PDF documents based on a user-selected topic using Large Language Models (LLMs).

## Features

* Upload PDF documents
* Extract text from PDFs
* Generate topic-focused slide content using LLMs
* Create slide outlines automatically
* Generate PowerPoint presentations (.pptx)
* Add relevant images to slides
* FastAPI backend for API integration
* Modular architecture for easy customization

## Project Structure

```text
backend/
├── controllers/
├── models/
├── prompts/
├── services/
├── utils/
├── output/
├── uploads/
├── main.py
├── requirements.txt
└── .gitignore

ppt-generator/
├── generatePpt.js
├── package.json
├── package-lock.json
└── slides.json
```

## Technology Stack

### Backend

* Python
* FastAPI
* Ollama
* Qwen 2.5 LLM
* PDF Processing Libraries

### PPT Generation

* Node.js
* PptxGenJS

### Image Integration

* Pexels API

## Workflow

```text
PDF Upload
    ↓
Text Extraction
    ↓
Topic Selection
    ↓
LLM Processing (Qwen/Ollama)
    ↓
Slide Content Generation
    ↓
slides.json Creation
    ↓
generatePpt.js
    ↓
PPTX Generation
    ↓
Generated Presentation
```

## Installation

### Clone Repository

```bash
git clone https://github.com/Abhiramsai20/llm-ppt-generator.git
cd llm-ppt-generator
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Install Node Dependencies

```bash
cd ppt-generator
npm install
```

### Run FastAPI Backend

```bash
uvicorn main:app --reload
```

## API Endpoint

### Generate Slides

```http
POST /generate-slides
```

Inputs:

* PDF File
* Topic

Output:

* Generated PowerPoint Presentation

## Future Enhancements

* RAG Integration
* Gemini API Support
* Better Image Retrieval
* Advanced Slide Templates
* Cloud Deployment
* Multi-language Support

## Author

Abhiram Sai

B.Tech Computer Science and Engineering

GITAM University, Visakhapatnam

