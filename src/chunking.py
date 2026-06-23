from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_text_splitter(chunk_size=300, chunk_overlap=50):
    """
    Create a RecursiveCharacterTextSplitter.
    """
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )


def chunk_documents(df, splitter):

    chunks = []

    for _, row in df.iterrows():

        split_text = splitter.split_text(row["cleaned_text"])

        for chunk in split_text:

            chunks.append({
                "complaint_id": row["complaint_id"],
                "product_category": row["product_category"],
                "chunk": chunk
            })

    return chunks