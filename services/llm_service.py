import ollama
import json


def generate_presentation(topic, content):

    content = content[:6000]

    prompt = f"""
You are an expert presentation designer.

TOPIC:
{topic}

CONTENT:
{content}

Requirements:

- Generate exactly 8 slides.
- Create professional presentation slides.
- Avoid repeating information.
- Use professional business language.
- Summary maximum 25 words.
- Content maximum 120 words.
- Maximum 5 bullet points.
- Maximum 18 words per bullet.
- Explain concepts clearly.
- Include technical details when relevant.

Image Rules:

- need_image = true only when a visual improves understanding.

Use images for:
- Architecture
- Workflow
- Process
- System Design
- Applications
- Use Cases
- Real World Examples
- Industry Examples
- Future Trends
- Comparisons

Do not use images for:
- Introduction
- Overview
- Definitions
- Benefits
- Challenges
- Recommendations
- Summary
- Conclusion

Example Rules:

- Every slide with need_image = true must contain an example.
- Example maximum 30 words.
- Use realistic business, industry, or real-world examples.
- Slides with need_image = false may leave example empty.

Takeaway Rules:

- Include meaningful takeaway.
- Maximum 20 words.
- Do not repeat content.

IMPORTANT:

- Every slide must contain:
  - title
  - summary
  - content
  - bullets
  - takeaway
  - need_image

- Return ONLY valid JSON.
- Do not return markdown.
- Do not return explanations.
- Do not add text before or after JSON.
- Ensure valid JSON syntax.

Format:

{{
  "title": "Presentation Title",
  "slides": [
    {{
      "title": "Slide Title",
      "summary": "Maximum 25 words summary",
      "content": "Detailed explanation maximum 120 words",
      "bullets": [
        "Bullet point 1",
        "Bullet point 2",
        "Bullet point 3",
        "Bullet point 4",
        "Bullet point 5"
      ],
      "example": "",
      "takeaway": "Key takeaway maximum 20 words",
      "need_image": false
    }}
  ]
}}
"""

    print("Starting Ollama...")

    response = ollama.generate(
        model="qwen2.5:1.5b",
        prompt=prompt,
        format="json",
        options={
            "temperature": 0
        }
    )

    print("Ollama Finished")

    result = response["response"]

    try:

        start = result.find("{")
        end = result.rfind("}") + 1

        json_text = result[start:end]

        return json.loads(json_text)

    except Exception as e:

        print("JSON ERROR:", e)
        print(result)

        return {
            "title": topic,
            "slides": [
                {
                    "title": "Generation Error",
                    "summary": "",
                    "content": "Failed to generate presentation",
                    "bullets": [],
                    "example": "",
                    "takeaway": "",
                    "need_image": False
                }
            ]
        }


def generate_image_prompt(title, content):

    prompt = f"""
You are an expert PowerPoint infographic designer.

Create a professional image generation prompt.

Rules:

- Professional PowerPoint infographic
- Corporate presentation design
- Clean vector graphics
- White background
- Blue accent colors
- Modern layout
- High quality
- Presentation ready
- Minimalistic design
- No watermark
- No text inside image
- No decorative elements
- Suitable for business presentations

If architecture:
- generate architecture diagram

If workflow:
- generate workflow diagram

If process:
- generate process flow diagram

If applications:
- generate business infographic

If use case:
- generate realistic professional illustration

If future trends:
- generate futuristic concept illustration

Slide Title:
{title}

Slide Content:
{content}

Return only the image prompt.
"""

    try:

        response = ollama.generate(
            model="qwen2.5:1.5b",
            prompt=prompt,
            options={
                "temperature": 0.3
            }
        )

        return response["response"].strip()

    except Exception as e:

        print("Image Prompt Error:", e)

        return title