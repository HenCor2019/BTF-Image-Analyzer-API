# This file is responsible for signing , encoding , decoding and returning JWTS
import time
from typing import Dict
import jwt
from decouple import config


JWT_ACCESS_SECRET = config("JWT_ACCESS_SECRET")
JWT_REFRESH_SECRET = config("JWT_REFRESH_SECRET")
JWT_ALGORITHM = config("ALGORITHM")


def token_response(access_token: str, refresh_token: str):
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }

# function used for signing the JWT string
def signJWT(user_id: str) -> Dict[str, str]:
    JWT_ACCESS_TOKEN_MIN = config("JWT_ACCESS_TOKEN_MIN")
    JWT_REFRESH_TOKEN_MIN = config("JWT_REFRESH_TOKEN_MIN")

    payload_access = {
        "user_id": user_id,
        "expires": float(JWT_ACCESS_TOKEN_MIN ) * 7
    }
    payload_refresh = {
        "user_id": user_id,
        "expires": float(JWT_REFRESH_TOKEN_MIN) * 60
    }
    access_token = jwt.encode(payload_access, JWT_ACCESS_SECRET, algorithm=JWT_ALGORITHM)
    refresh_token = jwt.encode(payload_refresh, JWT_REFRESH_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(access_token, refresh_token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_ACCESS_SECRET, algorithm=JWT_ALGORITHM)
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}

def decodeRefreshJWT(refresh_token: str) -> dict:
    try:
        decoded_token = jwt.decode(refresh_token, JWT_REFRESH_SECRET , algorithm=JWT_ALGORITHM)
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
