from datetime import datetime


from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    email: EmailStr
    password_hash: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class SignupRequest(LoginRequest):
    confirm_email: str
    confirm_password: str


class Session(BaseModel):
    user_id: int
    token: str
    expiry: datetime

