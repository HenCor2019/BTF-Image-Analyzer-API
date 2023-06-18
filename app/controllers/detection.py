from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import JSONResponse
import requests
import json
from app.auth.deps import get_current_user
from app.constants.tensorflow_url import DETECTION_MODEL_BASE_URL, MRI_VALIDATION_THRESHOLD, VALIDATION_MODEL_BASE_URL
from app.models.user import User
from app.utils.image_processing import read_image_from_file

router = APIRouter()

@router.post("/api/v1/analyze", summary="Use it to get an image predictions", tags=["Diagnostics"])
async def analyze_image(user: User = Depends(get_current_user), file: UploadFile = File(default=None)):
    try:
        normalized_image = await read_image_from_file(file)

        instances = normalized_image.reshape((1,)+normalized_image.shape).tolist()
        request_json = json.dumps({
             "signature_name": "serving_default",
             "instances": instances
        })
        response = requests.post(DETECTION_MODEL_BASE_URL, data=request_json)
        response.raise_for_status()
        response = response.json()

        predictions = response['predictions'][0]
        return JSONResponse(
            status_code=200,
            content={'tumor_detection':{'no_tumor':predictions[0],'tumor':predictions[1]}}
        )
    except:
        return JSONResponse(
            status_code=400,
            content={'message': 'Prediction failed'}
        )

@router.post("/api/v1/validate", summary="Use it to validate an image", tags=["Diagnostics"])
async def validate_image(user: User = Depends(get_current_user), file: UploadFile = File(default=None)):
    try:
        normalized_image = await read_image_from_file(file)

        instances = normalized_image.reshape((1,)+normalized_image.shape).tolist()
        request_json = json.dumps({
             "signature_name": "serving_default",
             "instances": instances
        })
        response = requests.post(VALIDATION_MODEL_BASE_URL, data=request_json)
        response.raise_for_status()
        response = response.json()

        mri_image_percentage = response['predictions'][0][0]
        is_valid_mri_image = 1.0 - float(mri_image_percentage) > float(MRI_VALIDATION_THRESHOLD)
        return JSONResponse(
            status_code=200,
            content={'is_valid_mri_image': is_valid_mri_image, 'percentage': mri_image_percentage }
        )
    except:
        return JSONResponse(
            status_code=400,
            content={'is_valid_mri_image': False, 'percentage': -1 }
        )
