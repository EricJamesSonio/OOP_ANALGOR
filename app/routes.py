from fastapi import APIRouter, HTTPException
from services import UserService
from repositories import UserRepository
from models import User

router = APIRouter()
user_service = UserService(UserRepository())


@router.get("/users", response_model=list[User])
def get_users():
    return user_service.get_users_above_age(28)


@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = user_service.get_user(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")
