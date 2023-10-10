from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: int
    email: str
    date_created: datetime
    date_modified: datetime

    class Config:
        orm_mode = True


class CardCreate(BaseModel):
    label: str
    card_no: int
    status: str

    class Config:
        orm_mode = True


class CardBase(BaseModel):
    id: int
    label: str
    card_no: int
    user_id: int


class TransactionBase(BaseModel):
    id: int
    card_id: int
    amount: int
    description: str

class TransactionData(BaseModel):
    active_card_count: int
    active_card_total_spending: int
    passive_card_count: int
    passive_card_total_spending: int


class TransactionCreate(BaseModel):
    card_id: int
    amount: int
    description: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class CustomOAuth2LoginForm(BaseModel):
    email: EmailStr
    password: str
