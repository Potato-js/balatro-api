import json

from fastapi import APIRouter
from pathlib import Path
from models.jokers import Card
from typing import List

router = APIRouter(prefix="/cards", tags=["Cards"])

base_path = Path("data/cards")


@router.get("/jokers", response_model=List[Card])
async def get_jokers():
    return _load_cards("jokers.json")


@router.get("/planets", response_model=List[Card])
async def get_planets():
    return _load_cards("planets.json")


@router.get("/tarots", response_model=List[Card])
async def get_tarots():
    return _load_cards("tarots.json")


@router.get("/spectrals", response_model=List[Card])
async def get_spectrals():
    return _load_cards("spectrals.json")


def _load_cards(filename: str) -> List[Card]:
    file_path = base_path / filename
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
