from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, UniqueConstraint
from .config import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    date_created = Column(TIMESTAMP(timezone=True),
                          nullable=False, server_default=text('now()'))
    date_modified = Column(TIMESTAMP(timezone=True), nullable=False,
                           server_default=text('now()'), onupdate=text('now()'))


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(100), nullable=False, default="SYSTEM_CARD")
    card_no = Column(BigInteger, nullable=False)
    status = Column(String(15), nullable=False, default="PASSIVE")
    date_created = Column(TIMESTAMP(timezone=True),
                          nullable=False, server_default=text('now()'))
    date_modified = Column(TIMESTAMP(timezone=True), nullable=False,
                           server_default=text('now()'), onupdate=text('now()'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    __table_args__ = (
        UniqueConstraint('user_id', 'card_no', name='unique_card'),
    )


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, ForeignKey("cards.id", ondelete="CASCADE"))
    amount = Column(Integer, nullable=False)
    description = Column(String(200), nullable=False)
    date_created = Column(TIMESTAMP(timezone=True),
                          nullable=False, server_default=text('now()'))
    date_modified = Column(TIMESTAMP(timezone=True), nullable=False,
                           server_default=text('now()'), onupdate=text('now()'))
