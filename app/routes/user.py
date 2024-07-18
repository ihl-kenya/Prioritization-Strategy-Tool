from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import *
from app.config import get_db
from app.services.user import UserServices


def create_user_router() -> APIRouter:
    user_router = APIRouter(prefix="/users", tags=["User endpoints"])
    user_services = UserServices()

    @user_router.post("/new/", response_model=UserCreartedConfirmation)
    def create_new_user(user_details: UserCreate, db: Session = Depends(get_db)):
        msg = user_services.new_user(user_details=user_details, db=db)
        msg_formatted = UserCreartedConfirmation(message=msg)
        return msg_formatted

    return user_router
