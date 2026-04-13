from app.services.retrieval_service import retrieve_relevant_news
from app.services.summarizer_service import summarize_news

query = "latest AI news"

docs = retrieve_relevant_news(query)
summary = summarize_news(docs)

print(summary)
