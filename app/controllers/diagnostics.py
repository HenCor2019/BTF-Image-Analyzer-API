from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi_pagination import LimitOffsetPage, paginate
from app.auth.deps import get_current_user

from app.models.user import Doctor, User
from app.schemas.diagnostics import DiagnosticOut, UpdateDiagnosticDto
from app.services.diagnostics import DiagnosticService
from app.utils.success_messages import get_fail_diagnostic_message, get_success_diagnostic_message


router = APIRouter()

@router.get("/api/v1/diagnostics/me", summary="Use it search all diagnostics", tags=["Diagnostics"], response_model=LimitOffsetPage[DiagnosticOut])
async def get_all(q: str = "", user: User = Depends(get_current_user)):
    doctor: Doctor = user.doctors[0]
    diagnostics = DiagnosticService().find_all(doctor.id, q)
    return paginate(diagnostics)

@router.patch("/api/v1/diagnostics/{diagnostic_id}/evaluate", summary="Use it evaluate one diagnostics", tags=["Diagnostics"])
async def evaluate(diagnostic_id: str, update_dto: UpdateDiagnosticDto, user: User = Depends(get_current_user), lan: str = "en"):
    doctor: Doctor = user.doctors[0]
    try:
        DiagnosticService().evaluate(doctor.id, diagnostic_id, update_dto, lan)
        message = get_success_diagnostic_message(lan)
        return JSONResponse(
            status_code=400,
            content={'is_valid_mri_image': False, 'percentage': -1, 'message': message}
        )
    except:
        message = get_fail_diagnostic_message(lan)
        return JSONResponse(
            status_code=400,
            content={'is_valid_mri_image': False, 'percentage': -1, 'message': message}
        )
