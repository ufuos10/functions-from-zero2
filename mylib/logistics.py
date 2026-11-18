"""
This module deals with logistics and calculates distances between two points
and the time it takes to travel and other logistics questions for a given speed.
"""
from geopy import distance

# Coordinates (latitude, longitude) for 20 cities in the USA
cities = {
    "New York": (40.7128, -74.0060),
    "Los Angeles": (34.0522, -118.2437),
    "Chicago": (41.8781, -87.6298),
    "Houston": (29.7604, -95.3698),
    "Phoenix": (33.4484, -112.0740),
    "Philadelphia": (39.9526, -75.1652),
    "San Antonio": (29.4241, -98.4936),
    "San Diego": (32.7157, -117.1611),
    "Dallas": (32.7767, -96.7970),
    "San Jose": (37.3382, -121.8863),
    "Austin": (30.2672, -97.7431),
    "Jacksonville": (30.3322, -81.6557),
    "Fort Worth": (32.7555, -97.3308),
    "Columbus": (39.9612, -82.9988),
    "Charlotte": (35.2271, -80.8431),
    "San Francisco": (37.7749, -122.4194),
    "Indianapolis": (39.7684, -86.1581),
    "Seattle": (47.6062, -122.3321),
    "Denver": (39.7392, -104.9903),
    "Washington": (38.9072, -77.0369)
}


def distance_between_two_points(point1, point2):
    """
    Calculate the distance between two points using geopy.

    :param point1: (latitude, longitude) of the first point.
    :param point2: (latitude, longitude) of the second point.
    :return: The distance in miles between the two points.
    """
    return distance.distance(point1, point2).miles


def get_city_coordinates(city):
    """
    Get the coordinates of a city.

    :param city: The name of the city.
    :return: (latitude, longitude) of the city, or None if the city is not found.
    """
    return cities.get(city)


def total_distance(city_names):
    """
    Calculate the total distance between a list of cities.

    :param city_names: A list of city names.
    :return: The total distance in miles, visiting the cities in the given order.
    """
    total_dist = 0
    for city1, city2 in zip(city_names, city_names[1:]):
        point1 = get_city_coordinates(city1)
        point2 = get_city_coordinates(city2)
        if point1 is None or point2 is None:
            raise ValueError(f"One or both cities not found: {city1}, {city2}")
        total_dist += distance_between_two_points(point1, point2)
    return total_dist


if __name__ == "__main__":
    print(total_distance(["New York", "Chicago"]))