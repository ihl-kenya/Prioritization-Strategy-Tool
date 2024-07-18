from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas import *
from app.config import get_db
from app.services.user import UserServices


def create_user_router() -> APIRouter:
    user_router = APIRouter(prefix="/users", tags=["User endpoints"])
    user_services = UserServices()

    @user_router.post("/register/", response_model=ActionConfirmation, status_code=status.HTTP_201_CREATED)
    async def create_new_user(user_details: UserCreate, db: Session = Depends(get_db)):
        msg = user_services.new_user(user_details=user_details, db=db)
        msg_formatted = ActionConfirmation(message=msg)
        return msg_formatted

    @user_router.post("/login/", response_model=ActionConfirmation, status_code=status.HTTP_200_OK)
    async def login_user(credentials: UserLogin, db: Session = Depends(get_db)):
        msg = user_services.login_user(credentials=credentials, db=db)
        msg_formatted = ActionConfirmation(message=msg)
        return msg_formatted

    @user_router.put("/update/", response_model=ActionConfirmation, status_code=status.HTTP_201_CREATED)
    async def update_user(email: str, user_details: UserCreate, db: Session = Depends(get_db)):
        msg = user_services\
            .update_user(email=email, user_details=user_details, db=db)

        msg_formatted = ActionConfirmation(message=msg)
        return msg_formatted

    @user_router.delete("/delete_user/", response_model=ActionConfirmation)
    async def delete_user(email: str, db: Session = Depends(get_db)):
        msg = user_services.remove_user(email=email, db=db)
        msg_formatted = ActionConfirmation(message=msg)
        return msg_formatted

    return user_router
