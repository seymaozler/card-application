from .. import schemas, models, utils
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..config import get_db

from ..service import user_create, card_create, write_to_redis

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = user_create(user, db)
    new_card = card_create(new_user, db, default=True)
    data = {
        "hashed_password": new_user.password,
        "id": new_user.id,
        "status": new_card.status
    }
    write_to_redis(new_user.email, data)

    return new_user
