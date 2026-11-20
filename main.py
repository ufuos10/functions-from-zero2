from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

from mylib.logistics import (
    cities,
    get_city_coordinates,
    total_distance,
    travel_time,
)

app = FastAPI()

class City(BaseModel):
    name:str


@app.post("/cities/lookup")
async def lookup_city(city: City):
    """Look up a city's coordinates from a JSON body."""
    coords = get_city_coordinates(city.name)
    if coords is None:
        raise HTTPException(status_code=404, detail=f"City not found: {city.name}")
    return {"city": city.name, "latitude": coords[0], "longitude": coords[1]}

@app.post("/")
async def root():
    """Home Page with GET HTTP Method"""
    return {"message": "Hello Logistics INC"}


@app.post("/cities")
async def get_cities():
    """Get the list of available cities."""
    return {"cities": list(cities)}


@app.post("/cities/{city}")
async def city_coordinates(city: str):
    """Get the coordinates of one city."""
    coords = get_city_coordinates(city)
    if coords is None:
        raise HTTPException(status_code=404, detail=f"City not found: {city}")
    return {"city": city, "latitude": coords[0], "longitude": coords[1]}


@app.post("/distance/{city1}/{city2}")
async def distance(city1: str, city2: str):
    """Get the distance in miles between two cities."""
    try:
        miles = total_distance([city1, city2])
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    return {"city1": city1, "city2": city2, "miles": round(miles, 2)}


@app.post("/travel-time/{city1}/{city2}")
async def get_travel_time(city1: str, city2: str, speed: float = 60):
    """Estimate travel time in hours between two cities at a given speed (mph)."""
    try:
        hours = travel_time(city1, city2, speed)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    return {"city1": city1, "city2": city2, "speed": speed, "hours": round(hours, 2)}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")