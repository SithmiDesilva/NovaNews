# 📰 NovaNews — Real-Time News Aggregator & Summarization Platform using RAG

NovaNews is a **real-time news aggregation and intelligent summarization platform** built using **Retrieval-Augmented Generation (RAG)**.

The system continuously fetches live news from trusted RSS feeds and APIs, stores articles in a **vector database**, retrieves the most relevant content based on user-selected categories, and generates **context-aware summaries** using a Large Language Model (LLM).

It also includes a **modern React dashboard frontend** with category filtering, clickable article cards, source links, and automatic refresh.

---

## 🚀 Project Overview

In today’s digital world, users are overwhelmed by massive volumes of news content across multiple sources.

NovaNews solves this problem by providing:

* **real-time news ingestion**
* **semantic search**
* **AI-generated summaries**
* **category-based filtering**
* **live updates every 5 minutes**

Users can select topics such as:

* Artificial Intelligence
* Technology
* Sports
* Finance
* Politics
* Criminal Investigations

The system retrieves the most relevant articles and presents:

1. latest headlines
2. article snippets
3. source links
4. overall AI-generated summary

---

## 🎯 Key Features

### 📰 Live News Aggregation

Fetches latest news from live RSS feeds and news APIs.

### 🧠 Retrieval-Augmented Generation (RAG)

Uses vector retrieval + LLM summarization.

### 🔍 Semantic Search

Uses embeddings for meaning-based retrieval instead of keyword matching.

### 📚 Vector Database

Stores news embeddings in **ChromaDB**.

### 💻 Interactive Frontend Dashboard

Built with **React + Vite**.

### 🔄 Auto Refresh

Automatically updates the database every **5 minutes**.

### 🔗 Clickable Source Links

Users can open the full original article.

### 📂 Category Dropdown Filtering

Instant topic-based news exploration.

---

## 🏗️ System Architecture

```text
                         ┌─────────────────────────┐
                         │   Live News APIs / RSS  │
                         │   BBC, CNN, Tech Feeds  │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │   News Scraper Service   │
                         │   feedparser / APIs      │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │ Text Cleaning + Parsing  │
                         │ title + snippet + link   │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │ Embedding Generator      │
                         │ SentenceTransformer      │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │ ChromaDB Vector Store    │
                         │ documents + metadata     │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │ Semantic Retrieval       │
                         │ top-k similarity search  │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │ LLM Summarization        │
                         │ OpenAI GPT               │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │ React Dashboard UI       │
                         │ headlines + summary      │
                         └─────────────────────────┘
```

---

## 🧠 RAG Workflow

NovaNews follows a standard Retrieval-Augmented Generation pipeline.

### Step 1 — Retrieval

Relevant news articles are retrieved from ChromaDB using semantic similarity search.

### Step 2 — Augmentation

Retrieved documents are passed as context to the LLM.

### Step 3 — Generation

The LLM generates an overall summary using only the retrieved context.

This ensures grounded, context-based responses.

---

## 🛠️ Tech Stack

### Backend

* **FastAPI**
* **Uvicorn**
* **APScheduler**

### Frontend

* **React**
* **Vite**
* **JavaScript**

### NLP / Embeddings

* **Sentence Transformers**
* `all-MiniLM-L6-v2`

### Vector Database

* **ChromaDB**

### LLM

* **OpenAI GPT API**

### News Sources

* **RSS feeds**
* **News APIs**

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
│   │   ├── summarizer_service.py
│   │   └── news_updater_service.py
│   │
│   └── utils/
│
├── chroma_db/
│
├── novanews-frontend/
│   ├── src/
│   │   └── App.jsx
│   └── package.json
│
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙️ Installation

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

Activate:

```bash
.venv\Scripts\activate
```

---

### Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

### Install Frontend Dependencies

```bash
cd novanews-frontend
npm install
```

---

## ▶️ Running the System

### Start Backend

```bash
uvicorn app.main:app --reload
```

Runs on:

```text
http://127.0.0.1:8000
```

---

### Start Frontend

```bash
cd novanews-frontend
npm run dev
```

Runs on:

```text
http://localhost:5173
```

---

## 🔄 Automatic Live News Updates

NovaNews automatically fetches and stores fresh news every **5 minutes** using APScheduler.

This includes:

* fetching latest articles
* embedding generation
* vector storage
* duplicate prevention

No manual database population is required.

---

## 🌐 Frontend Features

### Category Dropdown

Select news topics instantly.

### Article Cards

Displays clean clickable news cards.

### Source Links

Open original news articles directly.

### Overall Summary

AI-generated summary of displayed articles.

### Auto Refresh

Frontend and backend both support live refresh.

---

## 📡 API Endpoint

### Get News by Topic

```http
GET /news?topic=AI
```

Response:

```json
{
  "topic": "AI",
  "articles": [
    {
      "headline": "...",
      "snippet": "...",
      "source_link": "..."
    }
  ],
  "summary": "..."
}
```

---

## 🚀 Future Enhancements

* user authentication
* personalized saved topics
* sentiment analysis
* breaking news alerts
* thumbnail images
* dark mode UI
* trending topics section
* news credibility scoring
* multilingual summarization

---

## 🎓 Learning Outcomes

This project demonstrates strong understanding of:

* Retrieval-Augmented Generation (RAG)
* semantic search
* vector databases
* embedding pipelines
* real-time data ingestion
* backend API engineering
* frontend dashboard development
* production scheduling systems

---

## 📌 Status

✅ Fully functional backend
✅ Live frontend dashboard
✅ Auto-updating vector database
🚀 Production-ready architecture

---

## 👩‍💻 Author

Developed as a full-stack AI + Data Science project to demonstrate real-time RAG system design, semantic retrieval, and live dashboard engineering.
