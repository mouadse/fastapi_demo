import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/weather")
def get_weather(request: Request, url: str):
    # Fetch the HTML content from the provided URL
    response = requests.get(url)
    html = response.text

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Extract the temperature value
    temperature = soup.find("span", {"class": "temp__value"}).text

    # Extract the weather condition
    weather_condition = soup.find("div", {"class": "link__condition"}).text

    # Extract the feels_like value
    feels_like = soup.find("span", {"class": "term__value_with-unit"}).text

    # Render the HTML template with the weather information
    context = {"temperature": temperature, "weather_condition": weather_condition, "feels_like": feels_like, }
    return templates.TemplateResponse("weather.html", {"request": request, **context})
