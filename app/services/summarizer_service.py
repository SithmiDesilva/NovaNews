from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_news(documents):
    context = "\n".join(documents)

    prompt = f"""
    Summarize the following latest news articles:

    {context}

    Provide concise bullet points.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
