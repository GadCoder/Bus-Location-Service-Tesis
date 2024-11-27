import geopy.distance


def calculate_distance_from_user(
    user_lat: float, user_long: float, bus_lat: float, bus_long: float
) -> float:
    """
    Calculate the distance between the user and the bus
    """
    user_cords = (user_lat, user_long)
    bus_cords = (bus_lat, bus_long)

    distance_from_user = geopy.distance.geodesic(user_cords, bus_cords).km
    return distance_from_user
