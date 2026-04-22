import os
import smtplib
import logging
from email.mime.text import MIMEText
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def send_email():
    EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    date = datetime.utcnow().strftime('%Y-%m-%d')
    subject = f'Daily Tech News - {date}'
    # Prepare MIMEText message with HTML content
    body = "<html><body><h1>Your Daily Tech News</h1></body></html>"
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'rxq2112325066@gmail.com'

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            logging.info('Email sent successfully')
    except Exception as e:
        logging.error(f'Failed to send email: {e}')

# Example usage
if __name__ == '__main__':
    send_email()