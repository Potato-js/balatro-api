from pydantic import BaseModel
from typing import List


class Card(BaseModel):
    name: str
    type: str
    rarity: str
    description: str
    effects: List[str]
    image_url: str
