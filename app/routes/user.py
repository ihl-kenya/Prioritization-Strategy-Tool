from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import *


def create_user_router() -> APIRouter:
    user_router = APIRouter(prefix="/user/", tags=["User endpoints"])

    @user_router.post("/new/", response_model=UserCreartedConfirmation)
    async def create_new_user(user_details: UserCreate, db: Session = Depends(get_db)):
        pass
