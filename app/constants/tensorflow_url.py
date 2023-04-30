from cv2 import os


TENSORFLOW_MODEL_BASE_URL = os.getenv("TENSORFLOW_MODEL_BASE_URL", "http://model:8501/v1/models/brain_tumor_detection:predict")
