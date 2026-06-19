import json
import subprocess
import os

from services.image_service import generate_image
from services.llm_service import generate_image_prompt


def generate_pptx(slides_data):

    if not slides_data:
        raise ValueError("slides_data is empty")

    image_folder = "output/images"

    os.makedirs(
        image_folder,
        exist_ok=True
    )

    image_keywords = [
        "architecture",
        "workflow",
        "process",
        "system",
        "design",
        "application",
        "applications",
        "use case",
        "example",
        "examples",
        "future",
        "trend",
        "trends",
        "comparison",
        "deployment",
        "network",
        "pipeline",
        "model",
        "cricket"
    ]

    for i, slide in enumerate(
        slides_data.get("slides", [])
    ):

        title = slide.get(
            "title",
            f"Slide {i+1}"
        )

        content = slide.get(
            "content",
            ""
        )

        slide_title = title.lower()

        llm_need_image = slide.get(
            "need_image",
            False
        )

        keyword_need_image = any(
            keyword in slide_title
            for keyword in image_keywords
        )

        need_image = (
            llm_need_image
            or keyword_need_image
        )

        if (
            need_image
            and not slide.get("example")
        ):
            slide["example"] = (
                f"Real-world implementation of {title}"
            )

        print("\n========================")
        print("Slide:", title)
        print("Need Image:", need_image)

        if not need_image:

            slide["image_path"] = ""
            continue

        image_prompt = generate_image_prompt(
            title,
            content
        )

        print("\nGenerated Prompt:")
        print(image_prompt)

        image_path = os.path.join(
            image_folder,
            f"slide_{i+1}.jpg"
        )

        try:

            generated = generate_image(
                image_prompt,
                image_path
            )

            print(
                "Generated Path:",
                generated
            )

            slide["image_path"] = (
                generated if generated else ""
            )

        except Exception as e:

            print(
                f"Image Error for slide {i+1}:",
                e
            )

            slide["image_path"] = ""

    with open(
        "ppt-generator/slides.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            slides_data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(
        "\nslides.json saved successfully"
    )

    try:

        subprocess.run(
            ["node", "generatePpt.js"],
            cwd="ppt-generator",
            check=True
        )

    except Exception as e:

        print(
            "PPT Generation Error:",
            e
        )

        raise

    return "output/generated_presentation.pptx"