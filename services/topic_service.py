def find_topic_content(pdf_text, topic):

    topic = topic.lower()

    paragraphs = pdf_text.split("\n")

    matched = []

    for paragraph in paragraphs:

        if topic in paragraph.lower():
            matched.append(paragraph)

    return "\n".join(matched)