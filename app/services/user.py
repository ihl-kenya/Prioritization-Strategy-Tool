from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.user import UserCreate
from models.users import Users

print(Users().email)


class UserServices:
    def __init__(self) -> None:
        pass

    @staticmethod
    def new_user(user_details: UserCreate, db: Session):
        db_user = db.query(Users).filter(
            Users.email == user_details.email).first()
        if db_user:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"email {user_details.email} already taken"
            )
        db_user = Users(
            email=user_details.email,
            password=user_details.password,
            access_level=user_details.access_level,
            approved=user_details.approved,
            org_id=user_details.org_id
        )
        try:
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return "User Created Successfully"
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"{e}"
            )
