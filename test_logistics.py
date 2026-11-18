import pytest

from mylib.logistics import (
    distance_between_two_points,
    get_city_coordinates,
    total_distance,
    print_cities,
    cities
)


def test_distance_between_two_points():
    ny_coords = get_city_coordinates("New York")
    la_coords = get_city_coordinates("Los Angeles")
    dist = distance_between_two_points(ny_coords, la_coords)
    assert dist == pytest.approx(2451, abs=1)


def test_total_distance():
    dist = total_distance(["New York", "Los Angeles", "Chicago"])
    assert dist == pytest.approx(4197, abs=1)


def test_total_distance_unknown_city():
    with pytest.raises(ValueError):
        total_distance(["New York", "Atlantis"])


def test_print_cities(capsys):
    print_cities()
    output = capsys.readouterr().out
    for city in cities:
        assert f"- {city}" in output