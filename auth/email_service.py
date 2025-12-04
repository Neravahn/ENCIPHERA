import smtplib
from email.mime.text import MIMEText
import random


SENDER_EMAIL = "enciphera@gmail.com"
APP_PASSWORD = "xtje drjd lvqy jbda"


def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp(receiver_email):
    otp = generate_otp()

    msg = MIMEText(f"Your Enciphera verification code is: {otp}")
    msg['Subject'] = "Email Verification"
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email


    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        server.quit()
        print('sent')
        return otp
    
    except Exception as e:
        print(str(e))
        return None