from typing import Annotated, List
from fastapi import APIRouter, Depends
from .. import schemas
from sqlalchemy.orm import Session
from ..config import get_db
from ..oauth2 import get_current_user, oauth2_schema

from ..service import list_card, card_create, card_update, card_delete

router = APIRouter(
    prefix="/card",
    tags=["Cards"]
)


@router.get("/", response_model=List[schemas.CardBase])
def card_list(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    print("card list e girdik", current_user.__dict__)
    cards = list_card(current_user, db)
    return cards


@router.post("/", response_model=schemas.CardBase)
def create_card(card: schemas.CardCreate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    new_card = card_create(current_user, db, card=card)
    return new_card


@router.put("/{card_id}", response_model=schemas.CardCreate)
def update_card(card_id: int, card: schemas.CardCreate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

    updated_card = card_update(current_user, db, card_id, card_object=card)
    return updated_card


@router.delete("/{card_id}")
def delete_card(card_id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    deleted_card = card_delete(current_user, db, card_id)

    return {"message": f"{deleted_card} deleted successfully"}
