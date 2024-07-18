from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.user import UserCreate, UserLogin
from models.users import Users
import bcrypt

print(Users().email)


class UserServices:
    def __init__(self) -> None:
        pass

    # -----------------------hash a password---------------#
    def hash_password(self, password: str) -> str:
        # salt ensures that the same passwords result in different hashes
        salt = bcrypt.gensalt()
        hashed_password = bcrypt\
            .hashpw(password=password.encode("utf-8"), salt=salt)

        return hashed_password.decode("utf-8")

    # -----------------add a new user to db ------------------------#
    def new_user(self, user_details: UserCreate, db: Session) -> str:
        # checking whether email is already registered in db
        db_user = db.query(Users).filter(
            Users.email == user_details.email).first()

        if db_user:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"email {user_details.email} already taken"
            )
        db_user = Users(
            email=user_details.email,
            password=self.hash_password(password=user_details.password),
            access_level=user_details.access_level,
            approved=user_details.approved,
            org_id=user_details.org_id
        )

        try:
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return "User Created Successfully"
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Could not create user"
            )

    # ---------------Verify login ----------------------#
    @staticmethod
    def login_user(credentials: UserLogin, db: Session) -> str:
        db_user = db.query(Users)\
            .filter(Users.email == credentials.email).first()

        if db_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found!"
            )
        hashed_password = db_user.password
        if not bcrypt.checkpw(credentials.password.encode("utf-8"), hashed_password.encode("utf-8")):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password"
            )
        return "Login successful"

    # -----------------Update a user's data in db---------------------------------#
    def update_user(self, email: str, user_details: UserCreate, db: Session) -> str:
        db_user = db.query(Users).filter(Users.email == email).first()
        if db_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with {email=} not found!"
            )

        db_user.email = user_details.email
        db_user.password = self.hash_password(user_details.password)
        db_user.access_level = user_details.access_level
        db_user.approved = user_details.approved
        db_user.org_id = user_details.org_id

        try:
            db.commit()
            db.refresh(db_user)
            return "User updated successfully"
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"org_id '{user_details.org_id}' is invalid"
            )

    @staticmethod
    def remove_user(email: str, db: Session) -> str:
        db_user = db.query(Users).filter(Users.email == email).first()

        if db_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with {email=} not found!"
            )
        try:
            db.delete(db_user)
            db.commit()
            return "User removed successfully"
        except Exception as e:
            print(f"{e}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Could not delete user"
            )
