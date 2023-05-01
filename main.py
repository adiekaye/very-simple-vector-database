import numpy as np
from collections import defaultdict
from typing import List, Tuple

def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

class VectorDatabase:
    def __init__(self):
        self.vectors = defaultdict(np.ndarray)

    def insert(self, key: str, vector: np.ndarray) -> None:
        self.vectors[key] = vector

    def search(self, query_vector: np.ndarray, k: int) -> List[Tuple[str, float]]:
        similarities = [(key, cosine_similarity(query_vector, vector)) for key, vector in self.vectors.items()]
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:k]

    def retrieve(self, key: str) -> np.ndarray:
        return self.vectors.get(key, None)

if __name__ == "__main__":
    # Create an instance of the VectorDatabase
    vector_db = VectorDatabase()

    # Insert vectors into the database
    vector_db.insert("vector_1", np.array([0.1, 0.2, 0.3]))
    vector_db.insert("vector_2", np.array([0.4, 0.5, 0.6]))
    vector_db.insert("vector_3", np.array([0.7, 0.8, 0.9]))

    # Search for similar vectors
    query_vector = np.array([0.15, 0.25, 0.35])
    similar_vectors = vector_db.search(query_vector, k=2)
    print("Similar vectors:", similar_vectors)

    # Retrieve a specific vector by its key
    retrieved_vector = vector_db.retrieve("vector_1")
    print("Retrieved vector:", retrieved_vector)
