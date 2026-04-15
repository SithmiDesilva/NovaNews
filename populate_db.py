from app.services.scraper_service import fetch_news
from app.services.vector_service import store_article

articles = fetch_news()

print("Fetched:", len(articles))

for i, article in enumerate(articles):
    store_article(str(i), article)

print("Done storing")
