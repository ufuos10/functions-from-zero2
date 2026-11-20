from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

from mylib.logistics import (
    cities,
    get_city_coordinates,
    total_distance,
    travel_time,
)

from mylib.wiki import (
    get_wiki_summary,
    get_wiki_keywords,
    search_wiki_pages,
    get_wiki_page,

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

@app.get("/")
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

@app.post("/keywords")
async def get_keywords(page: str, max_keywords: int = 10):
    """Get keywords from a Wikipedia page."""
    keywords = get_wiki_keywords(page, max_keywords)
    if keywords is None:
        raise HTTPException(status_code=404, detail=f"Wikipedia page not found: {page}")
    return {"page": page, "keywords": keywords}

@app.post("/wiki-summary")
async def get_summary(page: str):
    """Get the summary of a Wikipedia page."""
    summary = get_wiki_summary(page)
    if summary is None:
        raise HTTPException(status_code=404, detail=f"Wikipedia page not found: {page}")
    return {"page": page, "summary": summary}

@app.post("/wiki-search")
async def search_wiki(query: str, results: int = 5):
    """Search for Wikipedia pages matching a query."""
    titles = search_wiki_pages(query, results)
    return {"query": query, "results": titles}


@app.post("/wiki-page")
async def get_page(page: str):
    """Get a Wikipedia page."""
    wiki_page = get_wiki_page(page)
    if wiki_page is None:
        raise HTTPException(status_code=404, detail=f"Wikipedia page not found: {page}")
    return {"page": page, "title": wiki_page.title, "text": wiki_page.text}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")