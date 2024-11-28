import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, message, recipient):
    sender_email = "infra.monitor@example.com"
    password = "yourpassword"
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient, msg.as_string())

send_email_alert("Critical Alert", "CPU usage above 90%", "admin@example.com")
