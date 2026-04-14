import datetime
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")
url = "https://zenquotes.io/api/today"

response = requests.get(url)
data = response.json()
quote = data[0]['q']

today = datetime.date.today()
day_name = today.strftime("%A")


def send_email():
    if not all([SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL]):
        print("Error: One or more environment variables are missing.")
        return

    msg = MIMEMultipart()
    msg['Subject'] = f"Time for some motivation! 🍃☕"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    body = f"It's {day_name}! Time for some motivation! \n\n💡 Motivational Quote of the Day 💡\n\n{quote}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print("Check your email!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email()
