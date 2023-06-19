from cv2 import os


DETECTION_MODEL_BASE_URL = os.getenv("DETECTION_API_BASE_URL", "https://btf-model-ml-production.up.railway.app/v1/models/brain_tumor_detection:predict")
VALIDATION_MODEL_BASE_URL = os.getenv("VALIDATION_API_BASE_URL", "https://btf-model-validator-ml-production.up.railway.app/v1/models/brain_tumor_validator:predict")
MRI_VALIDATION_THRESHOLD = os.getenv("MRI_VALIDATION_THRESHOLD", 0.6)
