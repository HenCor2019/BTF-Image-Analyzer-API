from python_http_client import ServiceUnavailableError
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

async def send_mail(email):
    try:
        sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email(os.environ.get("SENDGRID_MAIL"))  # Change to your verified sender
        to_email = To(email)  # Change to your recipient
        subject = "A new contact is found"
        content = Content("text/plain", "Sending a contact email")
        mail = Mail(from_email, to_email, subject, content)

        mail_json = mail.get()
        sg.client.mail.send.post(request_body=mail_json)
        return
    except ValueError:
        raise ServiceUnavailableError("Cannot send email")
