import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


def email_gmail(message, subject, to_address, from_address=None, login_key="key.json"):
    """
    Send emails using gmail.
    :param message: The message to be sent with the email.
    :param subject: the subject of the email.
    :param to_address: address to send email to.
    :param from_address: address to send email from, defaults to login username if not specified.
    :param login_key: a json file containing the username and password information.
    """
    with open(login_key, "r") as f:
        data = json.load(f)
        username, password = data["username"], data["password"]
    if from_address is None:
        from_address = username
    formatted_message = f"From: {from_address}\r\nTo: {to_address}\r\nSubject: {subject}\r\n\r\n{message}"
    _gmail_server_send(username, password, from_address, to_address, formatted_message)


def email_gmail_with_attachment(message, subject, attachment, to_address, from_address=None, login_key="key.json"):
    """
    Send emails using gmail.
    :param message: The message to be sent with the email.
    :param subject: the subject of the email.
    :param attachment: the file to be attached with the email.
    :param to_address: address to send email to.
    :param from_address: address to send email from, defaults to login username if not specified.
    :param login_key: a json file containing the username and password information.
    """
    with open(login_key, "r") as f:
        data = json.load(f)
        username, password = data["username"], data["password"]

    if from_address is None:
        from_address = username
    msg = MIMEMultipart()
    msg["From"], msg["To"], msg["Subject"] = from_address, to_address, subject
    msg.attach(MIMEText(message, "plain"))

    payload = MIMEBase("application", "octet-stream")
    with open(attachment, "rb") as f:
        payload.set_payload(f.read())
        encoders.encode_base64(payload)
        payload.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment)}")
        msg.attach(payload)
    _gmail_server_send(username, password, from_address, to_address, msg.as_string())


def _gmail_server_send(username, password, from_address, to_address, message):
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_address, to_address, message)
    server.close()

