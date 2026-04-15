from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler
from app.routes.news import router as news_router
from app.services.updater_service import update_latest_news

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(news_router)

scheduler = BackgroundScheduler()

@app.on_event("startup")
def start_scheduler():
    print("🚀 Starting scheduler...")

    update_latest_news()   # initial load

    scheduler.add_job(
        update_latest_news,
        "interval",
        minutes=5
    )

    scheduler.start()

@app.on_event("shutdown")
def stop_scheduler():
    scheduler.shutdown()

@app.get("/")
def home():
    return {"message": "NovaNews RAG System Running"}
