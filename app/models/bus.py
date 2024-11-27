import uuid
from beanie import Indexed
from pydantic import BaseModel

class Bus(BaseModel):
    bus_identifier: uuid.UUID
    plate: str
    company_id: int
    route_id: int
