from fastapi import FastAPI, UploadFile, File
import requests
import json
from app.constants.tensorflow_url import TENSORFLOW_MODEL_BASE_URL
from app.utils.image_processing import read_image_from_file

app = FastAPI()


@app.get("/healthcheck")
async def read_ok():
    return "ok"


@app.post("/api/v1/analyze")
async def analyze_image(file: UploadFile = File(...)):
    normalized_image = await read_image_from_file(file)

    instances = normalized_image.reshape((1,)+normalized_image.shape).tolist()
    request_json = json.dumps({
         "signature_name": "serving_default",
         "instances": instances
    })
    response = requests.post(TENSORFLOW_MODEL_BASE_URL, data=request_json)
    response.raise_for_status()
    response = response.json()

    predictions = response['predictions'][0]
    return {
        'tumor_detection': {
            'no_tumor':  predictions[0],
            'tumor': predictions[1]
        }
    }
