from python_http_client import ServiceUnavailableError
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from app.schemas.mailer import CreateMailDto

class Envs:
    EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    EMAIL_FROM = os.getenv('EMAIL_FROM')
    EMAIL_PORT = int(os.getenv('EMAIL_PORT'))
    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_FROM = os.getenv('EMAIL_FROM')


conf = ConnectionConfig(
    MAIL_USERNAME=Envs.EMAIL_USERNAME,
    MAIL_PASSWORD=Envs.EMAIL_PASSWORD,
    MAIL_PORT=Envs.EMAIL_PORT,
    MAIL_SERVER=Envs.EMAIL_HOST,
    MAIL_FROM=Envs.EMAIL_FROM,
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER='/code/app/templates/email'
)

async def send_mail(create_mail: CreateMailDto):
    try:
        message = MessageSchema(
            subject=create_mail.subject,
            recipients=[create_mail.email],
            subtype='html')
        fm = FastMail(conf)
        await fm.send_message(message, template_name='email.html')
    except:
        raise ServiceUnavailableError()
