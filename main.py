from fastapi import FastAPI
from routers import cards, decks, hands, tags

app = FastAPI(title="Balatro Game Data API")

app.include_router(cards.router)
app.include_router(decks.router)
app.include_router(hands.router)
app.include_router(tags.router)
