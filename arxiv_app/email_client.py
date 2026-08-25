import smtplib
import ssl
from email.message import EmailMessage


def send_email(
    subject: str,
    body: str,
    sender: str,
    recipient: str,
    app_password: str,
) -> None:

    context = ssl.create_default_context()

    msg = EmailMessage()
    msg.set_content(body)

    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10, context=context) as server:
        server.login(sender, app_password)
        server.send_message(msg)
