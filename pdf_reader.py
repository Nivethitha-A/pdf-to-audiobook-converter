import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from PDF page by page
    """
    text = ""
    doc = fitz.open(pdf_path)

    for page in doc:
        page_text = page.get_text().strip()
        if page_text:
            text += page_text + "\n"

    doc.close()
    return text
