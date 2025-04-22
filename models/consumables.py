from pydantic import BaseModel

# from typing import List, Optional


class Consumables(BaseModel):
    name: str
    type: str
    description: str
    image_url: str
