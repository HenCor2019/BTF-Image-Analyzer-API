from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List

from app.services.user import UserService
from app.schemas.user import UserCreate, UserPassword, User

router = APIRouter()

@router.post("/users")
def create_user(user: UserCreate):
    db_user = UserService().create_user(user)
    return db_user

@router.get("/users", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100):
    users = UserService().get_users(skip=skip, limit=limit)
    return jsonable_encoder(users, exclude={"password"})

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    db_user = UserService().get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return jsonable_encoder(db_user, exclude={"password"})

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserPassword):
    db_user = UserService().update_user(user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return jsonable_encoder(db_user, exclude={"password"})

@router.patch("/users/{user_id}/password", response_model=User)
def update_user_password(user_id: int, user: UserPassword):
    db_user = UserService().update_user(user_id, user)
    return {"message": "Password updated"}

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    db_user = UserService().delete_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

