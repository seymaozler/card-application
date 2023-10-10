from fastapi import FastAPI
from .config import engine
from .routers import user, auth, card, transaction
from . import models
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(card.router)
app.include_router(transaction.router)
