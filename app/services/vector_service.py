import chromadb
from app.services.embedding_service import generate_embedding

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="news_articles"
)

def store_article(article_id, text):
    embedding = generate_embedding(text)

    collection.add(
        ids=[article_id],
        embeddings=[embedding],
        documents=[text]
    )
