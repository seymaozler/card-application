from passlib.context import CryptContext
from .service import check_user_in_redis, write_to_redis, read_from_redis, card_status_update, list_card
from sqlalchemy.orm import Session
from fastapi import Depends
from .config import get_db
from . import models
from .oauth2 import get_current_user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(username, plain_password, db):
    if not check_user_in_redis(username):
        return None
    data = read_from_redis(username)
    if pwd_context.verify(plain_password, data["hashed_password"]):
        if data["status"] == "PASSIVE":
            data["status"] = "ACTIVE"
            write_to_redis(username, data)
            data = read_from_redis(username)
            card_status_update(data["id"],db)

        return data["id"]
    return False
