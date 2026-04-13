import feedparser

RSS_FEEDS = [
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://rss.cnn.com/rss/edition.rss",
    "https://feeds.feedburner.com/TechCrunch/"
]

def fetch_news():
    articles = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries:
            articles.append({
                "title": entry.title,
                "summary": entry.get("summary", ""),
                "link": entry.link,
                "published": entry.get("published", "")
            })

    return articles
