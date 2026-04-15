from fastapi import FastAPI
from app.routes.news import router as news_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(news_router)

@app.get("/")
def home():
    return {"message": "NovaNews RAG System Running"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
