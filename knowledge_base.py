# Create a minimal, no-LangChain knowledge_base.py using sentence-transformers and cosine similarity
import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

#Chunking breaks down data into small dataset 
def load_and_chunk_docs(path="rego_data", chunk_size=1000):
    all_chunks = []
    for fname in os.listdir(path):
        if fname.endswith(".txt"):
            with open(os.path.join(path, fname), "r", encoding="utf-8") as f:
                text = f.read()
                for i in range(0, len(text), chunk_size):
                    chunk = text[i:i+chunk_size].strip()
                    if chunk:
                        all_chunks.append(chunk)
    return all_chunks

#k is memory context
def get_top_chunks(query, k=3):
    chunks = load_and_chunk_docs()
    chunk_embeddings = model.encode(chunks)
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, chunk_embeddings)[0]
    top_indices = similarities.argsort()[-k:][::-1]
    return [chunks[i] for i in top_indices]

