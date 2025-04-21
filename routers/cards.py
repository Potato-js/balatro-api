import json

from fastapi import APIRouter
from pathlib import Path
from models.card import Card

router = APIRouter(prefix="/cards", tags=["Cards"])

data_path = Path("data/cards.json")


@router.get("/", response_model=list[Card])
async def get_cards():
    with open(data_path) as f:
        return json.load(f)
