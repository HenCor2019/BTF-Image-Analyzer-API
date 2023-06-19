from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List

from app.services.user import UserService
from app.schemas.user import UserCreate, UserPassword, User

router = APIRouter()

@router.post("/api/v1/sign-up", tags=["Users"])
def create_user(user: UserCreate):
    db_user = UserService().create_user(user)
    return db_user

@router.get("/api/v1/users", response_model=List[User], tags=["Users"])
def read_users(skip: int = 0, limit: int = 100):
    users = UserService().get_users(skip=skip, limit=limit)
    return jsonable_encoder(users, exclude={"password"})

@router.get("/api/v1/users/{user_id}", response_model=User, tags=["Users"])
def read_user(user_id: int):
    db_user = UserService().get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return jsonable_encoder(db_user, exclude={"password"})

@router.put("/api/v1/users/{user_id}", response_model=User, tags=["Users"])
def update_user(user_id: int, user: UserPassword):
    db_user = UserService().update_user(user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return jsonable_encoder(db_user, exclude={"password"})

@router.patch("/api/v1/users/{user_id}/password", response_model=User, tags=["Users"])
def update_user_password(user_id: int, user: UserPassword):
    db_user = UserService().update_user(user_id, user)
    return {"message": "Password updated"}

@router.delete("/api/v1/users/{user_id}", tags=["Users"])
def delete_user(user_id: int):
    db_user = UserService().delete_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

