# 📰 NovaNews 

NovaNews is a **Real-Time News Aggregation and Summarization System** built using **Retrieval-Augmented Generation (RAG)**.
The system continuously collects live news from trusted RSS feeds, stores them in a **vector database**, retrieves the most relevant articles based on user interests, and generates concise summaries using a Large Language Model (LLM).

This project demonstrates a **production-style RAG pipeline** with real-time ingestion, semantic retrieval, and intelligent summarization.

---

## 🚀 Project Overview

The goal of NovaNews is to solve the problem of **information overload in live news consumption**.

Instead of manually browsing multiple websites, users can simply enter a topic such as:

* Artificial Intelligence
* Finance
* Sports
* Criminal Investigations
* Politics

The system will:

1. Retrieve the latest relevant news articles
2. Semantically search them using embeddings
3. Generate an easy-to-read summary
4. Return the result instantly via API

This makes news consumption faster, personalized, and context-aware.

---

## 🎯 Key Features

* **Real-time news ingestion** from live RSS feeds
* **Semantic search** using vector embeddings
* **Retrieval-Augmented Generation (RAG)**
* **Topic-based personalized summaries**
* **FastAPI backend API**
* **ChromaDB vector storage**
* **LLM-powered summarization**
* Scalable and modular project structure

---

## 🏗️ System Architecture

```text
                ┌──────────────────────┐
                │  Live News Sources    │
                │ (BBC, CNN, Tech, etc) │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   RSS Feed Scraper    │
                │   (feedparser)        │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Text Preprocessing    │
                │ Chunking + Cleaning   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Embedding Generator   │
                │ SentenceTransformer   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │  ChromaDB Vector DB   │
                │ Store embeddings      │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ User Query / Topic    │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Semantic Retriever    │
                │ Similarity Search     │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ LLM Summarizer        │
                │ GPT / OpenAI API      │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Final News Summary    │
                └──────────────────────┘
```

---

## 🧠 How the RAG Pipeline Works

NovaNews follows the standard **RAG workflow**:

### Step 1 — Retrieval

Relevant articles are retrieved from the vector database using semantic similarity search.

### Step 2 — Augmentation

The retrieved articles are passed as context to the LLM.

### Step 3 — Generation

The LLM generates a concise summary using the retrieved context.

This improves factual grounding and ensures the response is based on live news data.

---

## 🛠️ Tech Stack

### Backend Framework

* **FastAPI**
* **Uvicorn**

### Data Ingestion

* **feedparser**
* RSS XML feeds

### NLP / Embeddings

* **Sentence Transformers**
* `all-MiniLM-L6-v2`

### Vector Database

* **ChromaDB**

### LLM / Summarization

* **OpenAI API**
* GPT models

### Language

* **Python 3.10+**

---

## 📂 Project Structure

```text
NovaNews/
│
├── app/
│   ├── main.py
│   ├── config.py
│   │
│   ├── routes/
│   │   └── news.py
│   │
│   ├── services/
│   │   ├── scraper_service.py
│   │   ├── embedding_service.py
│   │   ├── vector_service.py
│   │   ├── retrieval_service.py
│   │   └── summarizer_service.py
│   │
│   └── utils/
│       └── text_chunker.py
│
├── chroma_db/
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/yourusername/NovaNews.git
cd NovaNews
```

---

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

```bash
.venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Environment Variables

Create `.env`

```text
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Running the Project

```bash
uvicorn app.main:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

---

## 📡 API Endpoints

### Root Health Check

```http
GET /
```

Response:

```json
{
  "message": "NovaNews RAG System Running"
}
```

---

### Topic-Based News Summary

```http
GET /news?topic=AI
```

Example:

```http
GET /news?topic=criminal investigations
```

Response:

```json
{
  "topic": "criminal investigations",
  "summary": "..."
}
```

---

## 💡 Example Use Cases

* Personalized daily news digest
* Real-time event monitoring
* Topic-based intelligence dashboards
* Crime and legal news tracking
* Financial market updates
* AI / tech trend monitoring

---

## 🚀 Future Enhancements

* Frontend dashboard using React / Next.js
* User authentication
* Personalized topic subscriptions
* Breaking news alerts
* Sentiment analysis
* News credibility ranking
* Duplicate article detection
* Real-time WebSocket updates

---

## 🎓 Learning Outcomes

This project demonstrates practical understanding of:

* Retrieval-Augmented Generation (RAG)
* Semantic search
* Vector databases
* Embeddings
* LLM integration
* FastAPI backend development
* Real-time data pipelines

---

## 📌 Project Status

✅ Backend completed
✅ RAG pipeline working
🚀 Frontend dashboard planned

---

## 👩‍💻 Author

Developed as an AI and Data Science project to demonstrate real-time RAG system architecture and deployment-ready backend engineering.
