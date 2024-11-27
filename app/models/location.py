from typing import Tuple

from pydantic import BaseModel


class Location(BaseModel):
    type: str = "Point"
    coordinates: Tuple[float, float]
