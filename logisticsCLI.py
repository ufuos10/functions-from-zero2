#!/usr/bin/env python
from mylib.logistics import (
    distance_between_two_points,
    get_city_coordinates,
    travel_time,
)
import click


# build a click group to handle the logistics commands
@click.group()
def cli():
    """A logistics tool for calculating distances between cities."""


@cli.command("distance")
@click.argument("city1")
@click.argument("city2")
def distance(city1, city2):
    """Calculate the distance between two cities."""
    coords1 = get_city_coordinates(city1)
    coords2 = get_city_coordinates(city2)

    if not coords1 or not coords2:
        click.echo("One or both cities not found.")
        return

    dist = distance_between_two_points(coords1, coords2)
    click.secho(
        f"The distance between {city1} and {city2} is {dist:.2f} miles.", fg="green"
    )


@cli.command("travel-time")
@click.argument("city1")
@click.argument("city2")
@click.option(
    "--speed", default=60, help="The speed in miles per hour (default is 60 mph)."
)
def travel_time_command(city1, city2, speed):
    """Estimate the travel time between two cities by car."""
    try:
        hours = travel_time(city1, city2, speed)
        click.secho(
            f"The estimated travel time between {city1} and {city2} is {hours:.2f} hours.",
            fg="blue",
        )
    except ValueError as e:
        click.echo(e)


# Invoke the click command
if __name__ == "__main__":
    cli()
