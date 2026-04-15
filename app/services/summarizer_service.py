from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_news(documents):
    context = "\n\n".join(documents)

    prompt = f"""
You are a news summarization assistant.

Summarize ONLY the following retrieved news articles.
Do NOT mention inability to access the internet.
Do NOT mention external access limitations.

Retrieved articles:
{context}

Provide:
1. A short overall summary
2. 3 key bullet points
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
