
import geopy.distance


def calculate_distance_from_user(user_lat: float, user_long: float, bus_lat: float, bus_long: float) -> float:
    """
    Calculate the distance between the user and the bus
    """
    coords_1 = (user_lat, user_long)
    coords_2 = (bus_lat, bus_long)

    print(geopy.distance.geodesic(coords_1, coords_2).km)