from fastapi import APIRouter, Depends
from fastapi_pagination import LimitOffsetPage, paginate
from app.auth.deps import get_current_user

from app.models.user import Doctor, User
from app.schemas.diagnostics import DiagnosticOut
from app.services.diagnostics import DiagnosticService


router = APIRouter()

@router.get("/api/v1/diagnostics/me", summary="Use it search all diagnostics", tags=["Diagnostics"], response_model=LimitOffsetPage[DiagnosticOut])
async def get_all(q: str = "", user: User = Depends(get_current_user)):
    doctor: Doctor = user.doctors[0]
    diagnostics = DiagnosticService().find_all(doctor.id, q)
    return paginate(diagnostics)
