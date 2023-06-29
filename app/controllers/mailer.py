from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.libs.mailer import send_mail
from app.schemas.mailer import CreateMailDto
from app.utils.success_messages import get_fail_mailer_message, get_success_mailer_message


router = APIRouter()

@router.post("/api/v1/contact", summary="Use it to send some mail for contact us", tags=["Contact us"])
async def contact_with_us(create_mail: CreateMailDto, lan: str = "en"):
    try:
        await send_mail(create_mail)
        message = get_success_mailer_message(lan)
        return JSONResponse(status_code=200, content={'success': True, 'message': message})
    except:
        message = get_fail_mailer_message(lan)
        return JSONResponse(status_code=400, content={'success': False, 'message': message})
