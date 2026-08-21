import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

red = "\033[31;1m"
yellow = "\033[33;1m"
green = "\033[32;1m"
reset = "\033[0m"

# Load .env relative to script path
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

def get_ai_price(item_name: str):
    raw_key = os.environ.get("GROQ_API_KEY", "")
    clean_key = raw_key.strip().replace("\n", "").replace("\r", "")

    if not clean_key:
        print("Error: GROQ_API_KEY is missing or empty.")
        return

    client = Groq(api_key=clean_key)

    # Initialize conversation history with system instructions
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a savvy seller negotiating the price of '{item_name}'. "
                "Start by providing a realistic market estimate, then negotiate firmly "
                "Do Not ask for Bank details"
                "Do credit's cards or numbers"
                "only ask what you know you can provide"
                "but fairly with the user based on their counter-offers. Keep responses short."
                "EXACTLY: '[DEAL_CLOSED: $AMOUNT]' and wish them well."
            )
        },
        {
            "role": "user",
            "content": f"Hi, I want to buy {item_name}. What is your price?"
        }
    ]

    print(f"\n{green} looking up price for: {item_name} before negotiation so wait a sec pls {reset}")
    print(f"{green}(Type 'exit', 'quit', or 'bye' anytime to end the chat){reset}\n")

    # Start the AI chat loop
    while True:
        try:
            completion = client.chat.completions.create(
                model="groq/compound-mini",
                messages=messages,
                temperature=0.3
            )
            
            msg = completion.choices[0].message
            ai_response = msg.content or getattr(msg, 'reasoning', '') or "N/A"
            ai_response = ai_response.strip()

            # Append AI response to context history
            messages.append({"role": "assistant", "content": ai_response})
            print(f"\n{green}Seller (AI): {ai_response}{reset}\n")

        except Exception as e:
            print(f"Groq API Error: {e}")
            break

        # Get next offer or command from user
        user_input = input(f"{yellow}You: {reset}").strip()

        if user_input.lower() in ["exit", "quit", "bye", "go"]:
            print(f"\n{yellow}Ending negotiation. Thanks!{reset}")
            break

        # Append user response to context history
        messages.append({"role": "user", "content": user_input})