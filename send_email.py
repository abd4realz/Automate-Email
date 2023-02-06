import smtplib
import os
from email.mime.text import MIMEText
from email import utils

def send_email(subject, msg):
    try:
        with open(".env") as f:
            for line in f:
                key, value = line.strip().split("=")
                if key == "SENDER_EMAIL":
                    sender_email = value
                elif key == "SENDER_PASSWORD":
                    sender_password = value

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender_email, sender_password)
        message = MIMEText(msg)
        message['From'] = utils.formataddr(("Mabs Corp.", sender_email))
        message['to'] = "abdallahachimugu@gmail.com"
        message['subject'] = subject
        server.sendmail(sender_email, "abdallahachimugu@gmail.com", message.as_string())
        server.quit()
        print("Email sent successfully!")
    except:
        print("An error occurred while sending the email.")

subject = "Meeting Reminder"
msg = "This is a test message."

send_email(subject, msg)
