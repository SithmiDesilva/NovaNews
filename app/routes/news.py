from fastapi import APIRouter
from app.services.retrieval_service import retrieve_relevant_news
from app.services.summarizer_service import summarize_news

router = APIRouter()

@router.get("/news")
def get_news(topic: str):
    docs = retrieve_relevant_news(topic)
    summary = summarize_news(docs)

    return {
        "topic": topic,
        "summary": summary
    }
