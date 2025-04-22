from pydantic import BaseModel
from typing import List, Optional


class Jokers(BaseModel):
    name: str
    type: str
    rarity: Optional[str]
    description: str
    effects: List[str]
    image_url: str
