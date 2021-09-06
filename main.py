import smtplib
from email.message import EmailMessage

contacts = ["example1@gmail.com", "example2@gmail.com", "example3@gmail.com"]


msg = EmailMessage()
msg['Subject'] = "Subject"
msg['From'] = 'sender@gmail.com'
msg['To'] = "example1@gmail.com"
msg.set_content('This is a message')

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login('SENDER EMAIL', 'PASSWORD')

    smtp.send_message(msg)


