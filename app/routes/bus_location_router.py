from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, Security


from app.schemas.bus_location import BusLocationShow, BusLocationCreate, BusLocationQuery
from app.repository.bus_location import save_bus_location, get_buses_from_route, get_all_locations

router = APIRouter(prefix="/bus-location", tags=["Bus Location"])


@router.post("/create/", response_model=BusLocationShow)
async def register_bus_location(bus_location: BusLocationCreate):
    return await save_bus_location(bus_location=bus_location)


@router.get("/get-nearest-buses-from-route/", response_model=List[BusLocationQuery])
async def get_nearest_buses_from_route(
    company_id: int, route_id: int, latitude: float, longitude: float, delay_in_min: int, max_distance_in_km: int = 1
):
    return await get_buses_from_route(
        company_id=company_id,
        route_id=route_id,
        latitude=latitude,
        longitude=longitude,
        max_distance_in_km=max_distance_in_km,
        delay_in_min=delay_in_min
    )

@router.get("/get-all-buses-locations/", response_model=List[BusLocationShow])
async def get_all_buses_locations():
    return await get_all_locations()