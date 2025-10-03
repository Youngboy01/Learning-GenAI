from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ["HF_HOME"] = "D:/huggingface_cache"
from dotenv import load_dotenv
import numpy as np

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents = [
    "Rohit Sharma: Opens with aggressive strokeplay and flawless timing, turning starts into big scores.",
    "Virat Kohli: Elite chase master with exceptional footwork, consistency, and techno-savy pressure handling.",
    "Jasprit Bumrah: Unorthodox, pinpoint yorkers and deadly permutations in death overs.",
    "Ravindra Jadeja: Versatile all-rounder with sharp fielding, economical bowling, and lower-order prowess.",
    "Mohammed Shami: Seam movement and piercing lines late in innings, making every spell valuable.",
]
query = "Tell me about Virat Kohli"
doc_embeddings = embeddings.embed_documents(documents)
query_embeddings = embeddings.embed_query(query)


def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    n1 = np.linalg.norm(v1)
    n2 = np.linalg.norm(v2)
    similarity = dot_product / (n1 * n2)
    return similarity


similarities = [cosine_similarity(query_embeddings, doc) for doc in doc_embeddings]
for doc , score in zip(documents,similarities):
    print(f"Score: {score:.4f} | Document: {doc}")
    
'''
Outputs:
Score: 0.3821 | Document: Rohit Sharma: Opens with aggressive strokeplay and flawless timing, turning starts into big scores.
Score: 0.6083 | Document: Virat Kohli: Elite chase master with exceptional footwork, consistency, and techno-savy pressure handling.
Score: 0.2050 | Document: Jasprit Bumrah: Unorthodox, pinpoint yorkers and deadly permutations in death overs.
Score: 0.4170 | Document: Ravindra Jadeja: Versatile all-rounder with sharp fielding, economical bowling, and lower-order prowess.
Score: 0.4483 | Document: Mohammed Shami: Seam movement and piercing lines late in innings, making every spell valuable.
'''
