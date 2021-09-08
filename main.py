import smtplib
from email.message import EmailMessage


def send_email(contacts):
    for contact in contacts:
        msg = EmailMessage()
        msg['Subject'] = "Email Subject Goes here"
        msg['From'] = "yourEmail@gmail.com"
        msg['To'] = contacts[contact]
        msg.set_content('Example text body '
                        'Example text body '
                        'Example text body ')


        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login('yourEmail@gmail.com', 'yourEmailPassword')

            smtp.send_message(msg)


contacts = {

    "ExampleName": "exampleEmail@gmail.com",


}

send_email(contacts)
