from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text: str, chunk_size=500, overlap=100):
    """
    Split text into overlapping semantic chunks
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = splitter.split_text(text)

    return chunks
