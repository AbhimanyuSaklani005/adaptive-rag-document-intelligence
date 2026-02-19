import streamlit as st
from src.ingestion.loader import load_pdf
from src.ingestion.chunker import chunk_text

st.title("Adaptive RAG Document System")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:

    # Save temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = load_pdf("temp.pdf")
    chunks = chunk_text(text)

    st.success("PDF processed!")
    st.write("Characters:", len(text))
    st.write("Chunks:", len(chunks))
