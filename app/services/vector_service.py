import chromadb
from app.services.embedding_service import generate_embedding

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="news_articles"
)

def store_article(article_id, article):
    """
    article = {
        "title": ...,
        "summary": ...,
        "link": ...,
        "published": ...
    }
    """

    # convert structured article into text for embedding
    text = f"{article['title']}\n{article['summary']}"

    print("Embedding text:", text[:200])

    embedding = generate_embedding(text)

    collection.add(
        ids=[article_id],
        embeddings=[embedding],
        documents=[text],
        metadatas=[{
            "title": article["title"],
            "summary": article["summary"],
            "link": article["link"],
            "published": article["published"]
        }]
    )
