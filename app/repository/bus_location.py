from datetime import datetime, timedelta
from beanie.odm.operators.find.geospatial import Near
from app.models.bus_location import BusLocation


from app.schemas.bus_location import BusLocationCreate, BusLocationQuery


async def save_bus_location(bus_location: BusLocationCreate):
    bus_in_db = await BusLocation.find_one(BusLocation.bus.bus_identifier == bus_location.bus.bus_identifier)
    if not bus_in_db:
        bus_location_ = BusLocation(**bus_location.model_dump())
        await bus_location_.create()
        return bus_location_
    current_time = datetime.now()
    await bus_in_db.set({
            BusLocation.coordinates: bus_location.coordinates,
            BusLocation.timestamp: current_time,
            BusLocation.stop_name: bus_location.stop_name
        }
    )
    return bus_in_db

async def get_all_locations():
    return await BusLocation.find().project(BusLocationQuery).to_list()


async def get_buses_from_route(company_id: int, route_id: int, latitude: float, longitude: float, delay_in_min: int, max_distance_in_km: int = 1):
    time_delay = datetime.now() - timedelta(minutes=delay_in_min)
    print(time_delay)
    nearest_buses = await BusLocation.find(
        Near(BusLocation.coordinates, longitude, latitude, max_distance=max_distance_in_km*1000),
        BusLocation.bus.company_id == company_id,
        BusLocation.bus.route_id == route_id,
        BusLocation.timestamp >= time_delay
    ).project(BusLocationQuery).to_list()
    return nearest_buses

