from ..models import User
from fastapi import HTTPException


def user_create(user, db):
    email = db.query(User).filter(User.email == user.email).first()
    if email:
        raise HTTPException(
            status_code=409, detail="This email has already exists")
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
