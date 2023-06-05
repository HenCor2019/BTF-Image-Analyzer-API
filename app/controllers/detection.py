from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import JSONResponse
from python_http_client import ServiceUnavailableError
import requests
import json
from app.auth.auth_bearer import JWTBearer
from app.constants.tensorflow_url import DETECTION_MODEL_BASE_URL, MRI_VALIDATION_THRESHOLD, VALIDATION_MODEL_BASE_URL
from app.utils.image_processing import read_image_from_file

router = APIRouter()

@router.post("/{id}/analyze", dependencies=[Depends(JWTBearer())], tags=["Diagnostics"])
async def analyze_image(userId: str, file: UploadFile = File(default=None)):
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
        raise ServiceUnavailableError("Cannot analyze image")

@router.post("/{id}/validate", dependencies=[Depends(JWTBearer())], tags=["Diagnostics"])
async def validate_image(userId: str, file: UploadFile = File(default=None)):
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
