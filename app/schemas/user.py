from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    password: str
    access_level: str
    approved: bool


class UserCreate(User):
    org_id: str


class ActionConfirmation(BaseModel):
    message: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str
