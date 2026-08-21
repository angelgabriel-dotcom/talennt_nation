import os
from pathlib import Path
from dotenv import load_dotenv

# Get the exact folder where this file is located
BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

# Explicitly load the .env file from the exact directory
load_dotenv(dotenv_path=ENV_PATH)

key = os.environ.get("GROQ_API_KEY", "")

print("--- DEBUG RESULT ---")
print(f"Checking Path: {ENV_PATH}")
print(f"Key Found?: {bool(key)}")
print(f"Key Length: {len(key)}")