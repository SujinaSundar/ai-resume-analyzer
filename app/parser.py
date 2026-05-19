"""
pdf to text converter
"""
from pypdf import PdfReader

def extract_text(pdf_path):
    """
    extract text from resume
    """
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()
    return text
