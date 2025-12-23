def clean_text(text):
    """
    Cleans extracted text by removing extra spaces and newlines
    """
    if not text:
        return ""

    text = text.replace("\n", " ")
    text = " ".join(text.split())
    return text
