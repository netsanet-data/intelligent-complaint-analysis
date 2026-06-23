import faiss
import pandas as pd
import numpy as np


def create_faiss_index(embeddings):
    """
    Create a FAISS index from embeddings.
    """
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index


def save_vector_store(index, metadata, index_path, metadata_path):
    """
    Save the FAISS index and metadata.
    """
    faiss.write_index(index, index_path)

    metadata.to_csv(metadata_path, index=False)