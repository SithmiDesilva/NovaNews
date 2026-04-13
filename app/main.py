from fastapi import FastAPI
from app.services.retrieval_service import retrieve_relevant_news
from app.services.summarizer_service import summarize_news

app = FastAPI()

@app.get("/")
def home():
    return {"message": "News RAG System Running"}

@app.get("/news")
def get_news(topic: str):
    docs = retrieve_relevant_news(topic)
    summary = summarize_news(docs)

    return {
        "topic": topic,
        "summary": summary
    }
