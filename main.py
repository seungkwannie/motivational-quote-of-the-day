import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

SENDER_EMAIL = "stockpricetracker123@gmail.com"
SENDER_PASSWORD = "jlgv brdt uykg fjgm"
RECEIVER_EMAIL = "snowshoecatlover123@gmail.com"
url = "https://zenquotes.io/api/today"

response = requests.get(url)
data = response.json()
quote = data[0]['q']

today = datetime.date.today()
day_name = today.strftime("%A")

def send_email():
    msg = MIMEMultipart()
    msg['Subject'] = f"Time for some motivation! 🍃☕"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg.attach(MIMEText(f"It's {day_name}! Time for some motivation! \n\n💡 Motivational Quote of the Day 💡\n\n{quote}",
                        'plain'))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

if __name__ == "__main__":
    send_email()
    print("Check your email!!")
