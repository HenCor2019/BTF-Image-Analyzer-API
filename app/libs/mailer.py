from python_http_client import ServiceUnavailableError
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

from app.schemas.mailer import CreateMailDto

DEFAULT_CONTACT_EMAIL = 'henry200amaya@gmail.com'
async def send_mail(create_mail: CreateMailDto):
    contact_email = os.getenv("CONTACT_EMAIL", DEFAULT_CONTACT_EMAIL)
    try:
        sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email(os.environ.get("SENDGRID_MAIL"))
        to_email = To(contact_email)
        content_text = 'Hello, The user {name} is trying to contact us and he write this content for you.\n {content} \nPlease contact to the email {email}'.format(
            name=create_mail.name,
            content=create_mail.content,
            email=create_mail.email,
        )
        content = Content("text/plain", content_text)
        mail = Mail(from_email, to_email, create_mail.subject, content)

        mail_json = mail.get()
        sg.client.mail.send.post(request_body=mail_json)
    except ValueError:
        raise ServiceUnavailableError("Cannot send email")
