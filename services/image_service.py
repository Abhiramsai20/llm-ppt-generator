import requests
from urllib.parse import quote


def generate_image(prompt, save_path):

    print(f"\nGenerating image for prompt:")
    print(prompt)

    try:

        encoded_prompt = quote(prompt)

        url = (
            f"https://image.pollinations.ai/prompt/"
            f"{encoded_prompt}"
        )

        response = requests.get(
            url,
            timeout=120
        )

        print(
            f"Status Code: {response.status_code}"
        )

        if response.status_code == 200:

            with open(
                save_path,
                "wb"
            ) as f:

                f.write(
                    response.content
                )

            print(
                f"Saved: {save_path}"
            )

            return save_path

        print(
            "Image generation failed."
        )

        return None

    except Exception as e:

        print(
            "Image Service Error:",
            e
        )

        return None