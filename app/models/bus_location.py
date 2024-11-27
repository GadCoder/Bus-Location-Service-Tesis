from datetime import datetime

import pymongo
from beanie import Document

from app.models.bus import Bus
from app.models.location import Location


class BusLocation(Document):
    bus: Bus
    coordinates: Location
    timestamp: datetime = datetime.now()


    class Settings:
        name = "bus_location"
        indexes = [
            "bus.bus_id entifier",  # Unique index
            [("coordinates", pymongo.GEOSPHERE)],  # GEO index

        ]
