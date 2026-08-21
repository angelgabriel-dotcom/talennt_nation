import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

client = Groq(api_key=os.environ.get("GROQ_API_KEY", ""))

try:
    models = client.models.list()
    print("--- ACTIVE GROQ MODELS ---")
    for m in models.data:
        print(f"- {m.id}")
except Exception as e:
    print(f"Error fetching models: {e}")