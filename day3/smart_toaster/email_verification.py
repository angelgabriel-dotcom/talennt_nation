import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from pathlib import Path

# Explicitly target the .env file in the script's directory
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

class ToasterApp:
    def __init__(self, title: str, name: str, email: str):
        self.title = title
        self.name = name
        self.email = email
        
        # Pass the KEY names defined in your .env file
        self.sender_email = os.getenv("SENDER_EMAIL")
        self.app_password = os.getenv("SENDER_APP_PASSWORD")

    def send_notification(self) -> bool:
        if not self.sender_email or not self.app_password:
            print("Error: Missing SENDER_EMAIL or SENDER_APP_PASSWORD in .env file.")
            return False

        msg = MIMEText(f"Hello {self.name} {self.title},\n\nYour this email was sent to you from our office and i have been told you are the one gmaking our porn industry growing i thank God for you for helping us but if am a good person i just have to advice you that you should atleast calm down e the kill o!")
        msg["Subject"] = "Toaster Notification"
        msg["From"] = self.sender_email
        msg["To"] = self.email                

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(self.sender_email, self.app_password)
                server.send_message(msg)
            print("Email sent successfully!")
            return True
            
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

if __name__ == "__main__":
    app = ToasterApp("Mr.", "Student", "juliangravessen@gmail.com")
    app.send_notification()