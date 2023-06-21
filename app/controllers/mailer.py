from fastapi import APIRouter, Depends
from python_http_client import os
from starlette.responses import JSONResponse
from app.auth.deps import get_current_user

from app.libs.mailer import send_mail
from app.models.user import User
from app.schemas.mailer import CreateMailDto


router = APIRouter()

@router.post("/api/v1/contact", summary="Use it to send some mail for contact us", tags=["Contact us"])
async def contact_with_us(create_mail: CreateMailDto):
    try:
        await send_mail(create_mail)
        return JSONResponse(status_code=200, content={'success': True})
    except:
        return JSONResponse(status_code=400, content={'success': False})
