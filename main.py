from src.utils.file_picker import pick_pdf
from src.ingestion.loader import load_pdf

pdf_path = pick_pdf()

if not pdf_path:
    print("No file selected.")
    exit()

print("Selected:", pdf_path)

text = load_pdf(pdf_path)