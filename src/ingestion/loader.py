import fitz
import re

def clean_text(text: str) -> str:
    '''remove extra whitespace
    remove weird unicode artifacts
    remove repeated newlines '''
    text = re.sub(r'\s+', ' ', text)
    text = text.replace("\uf0b7", " ")
    text = re.sub(r'\n+', '\n', text)
    return text.strip()


def load_pdf(path: str) -> str:
    doc = fitz.open(path)
    all_text = []
    for page_num, page in enumerate(doc):
        text = page.get_text()
        if text:
            all_text.append(text)
    combined_text = "\n".join(all_text)
    cleaned = clean_text(combined_text)
    return cleaned
