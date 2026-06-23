from sentence_transformers import SentenceTransformer


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def load_embedding_model():
    """
    Load the embedding model.
    """
    return SentenceTransformer(MODEL_NAME)


def generate_embeddings(model, texts):
    """
    Generate embeddings for a list of text chunks.
    """
    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    return embeddings