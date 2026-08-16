import os
from groq import Groq

def get_ai_price(item_name: str) -> str:
    # 1. Fetch raw key from environment
    raw_key = os.environ.get("", "")
    
    # 2. Clean out any hidden newlines (\n), carriage returns (\r), or spaces
    clean_key = raw_key.strip().replace("\n", "").replace("\r", "")

    if not clean_key:
        print("Error: GROQ_API_KEY is missing or empty.")
        return "N/A"

    # 3. Pass clean key to Groq
    client = Groq(api_key=clean_key)

    prompt = (
        f"Give a realistic current market price estimate for item: '{item_name}'. "
        f"Return ONLY the estimated numeric price and currency (e.g. '$2,500' or '5,000 NGN'). "
        f"Do not write extra conversational text."
    )

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a precise price estimation assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Groq API Lookup failed: {e}")
        return "N/A"