#!/usr/bin/env python
 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
import os

# Load environment variables from .env file
if not load_dotenv():
    raise Exception(".env file not loaded successfully.")

# Fetch password from environment


def send_email(subject, body, to_email):
    from_email = os.getenv("GMAIL_USER")
    if not from_email:
        raise Exception("GMAIL_USER environment variable is not set.")
    
    from_password = os.getenv("GMAIL_PASSWORD")
    if not from_password:
        raise Exception("GMAIL_PASSWORD environment variable is not set.")

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Connect to the Gmail server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)

    # Send the email
    server.send_message(msg)
    server.quit()

# Example usage
send_email("Test Subject", "This is the body of the email", "ralph@goestenmeier.de")

