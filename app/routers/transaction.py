from typing import Annotated, List
from fastapi import APIRouter, Depends
from .. import schemas
from sqlalchemy.orm import Session
from ..config import get_db
from ..oauth2 import get_current_user, oauth2_schema
from ..service import transaction_create, detail_transactions, list_transactions
from fastapi import Query
from ..models import Transaction


router = APIRouter(
    prefix="/transaction",
    tags=["Transactions"]
)


@router.get("/", response_model=schemas.TransactionData)
def transaction_list(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    transactions = list_transactions(current_user, db)
    return transactions


@router.get("/details", response_model=List[schemas.TransactionBase])
def transaction_details(keyword: str = Query(None, title="description"), db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

    transactions = detail_transactions(current_user, db, keyword=keyword)
    return transactions


@router.post("/", response_model=schemas.TransactionCreate)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    new_transaction = transaction_create(
        db, current_user, transaction=transaction)
    return new_transaction
