import smtplib
from email.mime.text import MIMEText


def send_email_report():

    msg = MIMEText("Weekly GenAI Trend Report Generated.")

    msg["Subject"] = "GenAI Weekly Trend Report"
    msg["From"] = "your_email@gmail.com"
    msg["To"] = "recipient@email.com"

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login("your_email@gmail.com", "app_password")

    server.send_message(msg)

    server.quit()

    print("Email report sent.")