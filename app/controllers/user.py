from fastapi import APIRouter, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from typing import Annotated, List, Union

from app.services.user import UserService
from app.schemas.user import UserCreate, UserPassword, User
from app.utils.non_found import get_deleted_message, get_non_found_user_message, get_password_update_message

router = APIRouter()

@router.post("/api/v1/sign-up", tags=["Users"])
def create_user(user: UserCreate, lan: str = "en"):
    db_user = UserService().create_user(user, lan)
    return db_user

@router.get("/api/v1/users", response_model=List[User], tags=["Users"])
def read_users(skip: int = 0, limit: int = 100):
    users = UserService().get_users(skip=skip, limit=limit)
    return jsonable_encoder(users, exclude={"password"})

@router.get("/api/v1/users/{user_id}", response_model=User, tags=["Users"])
def read_user(user_id: int, lan: str = "en"):
    db_user = UserService().get_user(user_id)
    if db_user is None:
        non_found_error = get_non_found_user_message(lan)
        raise HTTPException(status_code=404, detail=non_found_error)
    return jsonable_encoder(db_user, exclude={"password"})

@router.put("/api/v1/users/{user_id}", response_model=User, tags=["Users"])
def update_user(user_id: int, user: UserPassword, lan: str = "en"):
    db_user = UserService().update_user(user_id, user)
    if db_user is None:
        non_found_error = get_non_found_user_message(lan)
        raise HTTPException(status_code=404, detail=non_found_error)
    return jsonable_encoder(db_user, exclude={"password"})

@router.patch("/api/v1/users/{user_id}/password", response_model=User, tags=["Users"])
def update_user_password(user_id: int, user: UserPassword, lan: str = "en"):
    UserService().update_user(user_id, user)
    message = get_password_update_message(lan)
    return {"message": message}

@router.delete("/api/v1/users/{user_id}", tags=["Users"])
def delete_user(user_id: int, lan: str = "en"):
    db_user = UserService().delete_user(user_id)
    if db_user is None:
        non_found_error = get_non_found_user_message(lan)
        raise HTTPException(status_code=404, detail=non_found_error)
    message = get_deleted_message(lan)
    return {"message": message}
