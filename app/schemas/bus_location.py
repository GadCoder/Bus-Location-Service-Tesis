import uuid
from datetime import datetime

from pydantic import BaseModel

from app.models.bus import Bus
from app.models.location import Location



class BusLocationBase(BaseModel):
    bus: Bus
    coordinates: Location



class BusLocationCreate(BusLocationBase):
    pass


class BusLocationShow(BusLocationBase):
    timestamp: datetime
    pass


class BusLocationQuery(BaseModel):
    bus_identifier: uuid.UUID
    plate: str
    latitude: float
    longitude: float
    timestamp: datetime
    class Settings:
        projection = {
            "bus_identifier": "$bus.bus_identifier",
            "plate": "$bus.plate",
            "timestamp": 1,
            "latitude": {"$arrayElemAt": ["$coordinates.coordinates", 1]},
            "longitude": {"$arrayElemAt": ["$coordinates.coordinates", 0]},
        }




