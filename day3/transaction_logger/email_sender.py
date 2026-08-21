import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from pathlib import Path
import datetime

RED = "\033[31;1m"
GREEN = "\033[32;1m"
RESET = "\033[0m"

# Load local .env relative to script location
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

class TransactionEmailer:
    def __init__(self, name: str, email: str, item_name: str, price: str):
        self.name = name
        self.email = email
        self.item_name = item_name
        self.price = price
        
        # Pull exact key names from .env
        self.sender_email = os.getenv("SENDER_EMAIL")
        self.app_password = os.getenv("SENDER_APP_PASSWORD")

    def send_receipt(self) -> bool:
        if not self.sender_email or not self.app_password:
            print(f"{RED}Error: SENDER_EMAIL or SENDER_APP_PASSWORD missing in .env{RESET}")
            return False

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        body = (
            f"Hello {self.name},\n\n"
            f"Here is your official transaction receipt:\n\n"
            f"----------------------------------------\n"
            f"Item: {self.item_name}\n"
            f"Price: ${self.price}\n"
            f"Date: {now}\n"
            f"----------------------------------------\n\n"
            f"Thank you for shopping with us!"
        )

        msg = MIMEText(body)
        msg["Subject"] = f"Transaction Receipt - {self.item_name}"
        msg["From"] = self.sender_email
        msg["To"] = self.email                

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(self.sender_email, self.app_password)
                server.send_message(msg)
                
            print(f"{GREEN}Receipt sent successfully to {self.email}!{RESET}")
            return True
            
        except Exception as e:
            print(f"{RED}Email dispatch failed: {e}{RESET}")
            return False

if __name__ == "__main__":
    emailer = TransactionEmailer("Julian", "juliangravessen@gmail.com", "MacBook Pro M2", "$1,850")
    emailer.send_receipt()