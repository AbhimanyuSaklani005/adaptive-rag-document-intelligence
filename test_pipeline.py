from src.ingestion.loader import load_pdf
from src.ingestion.chunker import chunk_text

pdf_path = r"C:\Users\abhi2\Downloads\Genomic DATA Blockchain.pdf"

text = load_pdf(pdf_path)
print("\nPDF loaded.")
print("Characters:", len(text))

chunks = chunk_text(text)

print("\nChunks created:", len(chunks))

print("\n--- FIRST CHUNK ---\n")
print(chunks[0])