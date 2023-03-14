import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()


@app.get("/weather")
def get_weather(url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    lat = soup.find("span", {"class": "latitude"}).text
    lon = soup.find("span", {"class": "longitude"}).text
    api_url = f"https://api.meteum.ai/v2/weather?lat={lat}&lon={lon}"
    api_response = requests.get(api_url)
    api_data = api_response.json()
    temperature = api_data["temperature"]["value"]
    wind_speed = api_data["wind_speed"]["value"]
    pressure = api_data["pressure"]["value"]
    description = api_data["description"]
    return {"temperature": temperature, "wind_speed": wind_speed, "pressure": pressure, "description": description}
