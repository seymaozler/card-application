from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import schemas, models, utils, oauth2
from ..config import get_db

router = APIRouter(
    tags=["Authentication"]
)


@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    id = utils.verify(user_credentials.username, user_credentials.password, db)
    if id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User could not found")
    if not id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    access_token = oauth2.create_access_token(data={"user_id": id})
    return {"access_token": access_token, "token_type": "bearer"}
