import os
import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

index = faiss.read_index(
    os.path.join(BASE_DIR, "vector_store", "complaints.index")
)

metadata = pd.read_csv(
    os.path.join(BASE_DIR, "vector_store", "chunk_metadata.csv")
)


def retrieve(question, k=5):

    question_embedding = model.encode([question])

    distances, indices = index.search(question_embedding, k)

    return metadata.iloc[indices[0]]