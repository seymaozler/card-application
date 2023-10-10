import random
from ..models import Card
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from ..config import get_db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func


def luhn_checksum(card_number):
    digits = list(map(int, card_number))
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for digit in even_digits:
        total += sum(divmod(digit * 2, 10))
    return total % 10


def generate_credit_card_number():
    first_six_digits = str(random.randint(400000, 499999))
    next_ten_digits = ''.join(random.choices('0123456789', k=10))

    card_number = first_six_digits + next_ten_digits
    checksum = luhn_checksum(card_number)
    last_digit = str((10 - checksum) % 10)

    return card_number + last_digit


def list_card(user, db):

    cards = db.query(Card).filter(
        Card.user_id == user.id,
        Card.status == "ACTIVE"
    ).all()
    return cards


def card_create(user, db, default=False, card=None):

    if default:
        new_card = Card(
            user_id=user.id,
            card_no=generate_credit_card_number(),
        )
    else:
        card.status = "ACTIVE"
        new_card = Card(**card.dict(), user_id=user.id)
    try:

        db.add(new_card)
        db.commit()
        db.refresh(new_card)
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=409, detail="This card number has already exists")
    return new_card


def card_update(user, db, card_id, card_object):

    card_query = db.query(Card).filter(Card.id == card_id)
    card = card_query.first()

    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    card_query.update(card_object.dict(), synchronize_session=False)
    db.commit()

    return card_object


def card_delete(user, db, card_id):
    card = db.query(Card).filter(Card.id == card_id,
                                 Card.status == "ACTIVE").first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    card.status = "DELETED"
    db.commit()
    return card_id


def card_status_update(user_id, db):
    card = db.query(Card).filter(Card.user_id == user_id).first()
    card.status = "ACTIVE"
    db.commit()
    db.refresh(card)
    return card
