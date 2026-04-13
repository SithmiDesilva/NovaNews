from app.services.vector_service import collection
from app.services.embedding_service import generate_embedding

def retrieve_relevant_news(query, top_k=5):
    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]
