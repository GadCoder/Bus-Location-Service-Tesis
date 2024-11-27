import uuid
from datetime import datetime

from pydantic import BaseModel

from app.models.bus import Bus
from app.models.location import Location



class BusLocationBase(BaseModel):
    bus: Bus
    coordinates: Location
    stop_name: str | None



class BusLocationCreate(BusLocationBase):
    pass


class BusLocationShow(BusLocationBase):
    timestamp: datetime
    pass


class BusLocationQuery(BaseModel):
    plate: str
    bus_identifier: uuid.UUID
    longitude: float
    latitude: float
    stop_name: str | None
    timestamp: datetime
    class Settings:
        projection = {
            "plate": "$bus.plate",
            "bus_identifier": "$bus.bus_identifier",
            "longitude": {"$arrayElemAt": ["$coordinates.coordinates", 0]},
            "latitude": {"$arrayElemAt": ["$coordinates.coordinates", 1]},
            "stop_name": 1,
            "timestamp": 1,
        }




