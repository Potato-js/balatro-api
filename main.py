from fastapi import FastAPI
from routers import card, decks, hands, tags, modifiers

app = FastAPI(title="Balatro Game Data API")

app.include_router(card.router)
# app.include_router(decks.router)
# app.include_router(hands.router)
# app.include_router(tags.router)
# app.include_router(modifiers.router)
