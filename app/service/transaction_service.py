from fastapi import HTTPException
from ..models import Transaction
from sqlalchemy import func
from ..models import Card, Transaction


def transaction_create(db, user, transaction):
    new_transaction = Transaction(**transaction.dict())
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction


def detail_transactions(user, db, keyword=None):
    transaction_query = db.query(Transaction)
    if keyword:
        transaction_query = transaction_query.filter(
            Transaction.description.like(f"%{keyword}%"))

    transactions = transaction_query.all()

    return transactions


def list_transactions(user, db):
    total_transactions = db.query(func.count(Transaction.id)).join(
        Card).filter(Card.user_id == user.id).scalar()
    if total_transactions == 0:
        raise HTTPException(
            status_code=404, detail="There is no transaction for this user")
    active_card_count = db.query(func.count()).filter(
        Card.user_id == user.id, Card.status == "ACTIVE").scalar()
    active_card_total_spending = db.query(func.sum(Transaction.amount))\
        .join(Card)\
        .filter(Card.status == "ACTIVE", Card.user_id == user.id)\
        .scalar()
    passive_card_count = db.query(func.count()).filter(
        Card.user_id == user.id, Card.status == "DELETED").scalar()
    passive_card_total_spending = db.query(func.sum(Transaction.amount))\
        .join(Card)\
        .filter(Card.status == "DELETED", Card.user_id == user.id)\
        .scalar()
    transaction_data = {
        "active_card_count": active_card_count,
        "active_card_total_spending": active_card_total_spending,
        "passive_card_count": passive_card_count,
        "passive_card_total_spending": passive_card_total_spending
    }
    return transaction_data
