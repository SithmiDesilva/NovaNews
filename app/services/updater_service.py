from app.services.scraper_service import fetch_news
from app.services.vector_service import store_article, collection

def update_latest_news():
    print("🔄 Fetching latest news...")

    articles = fetch_news()

    existing_ids = set(collection.get()["ids"])

    new_count = 0

    for i, article in enumerate(articles):
        article_id = article["link"]   # unique key

        if article_id not in existing_ids:
            store_article(article_id, article)
            new_count += 1

    print(f"✅ Added {new_count} new articles")
