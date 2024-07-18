from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: str
    password: str
    access_level: str
    approved: bool


class UserCreate(BaseModel):
    email: str
    password: str
    access_level: str
    approved: bool
    org_id: str


class ActionConfirmation(BaseModel):
    message: str
