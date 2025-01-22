import smtplib
from email.mime.text import MIMEText

def send_alert(user_email):
    msg = MIMEText("Suspicious activity detected on your account. Please check your account.")
    msg['Subject'] = "Account Alert"
    msg['From'] = "no-reply@bgmi.com"
    msg['To'] = user_email

    with smtplib.SMTP('smtp.example.com') as server:
        server.login("username", "password")
        server.send_message(msg)
