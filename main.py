import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/weather", response_class=HTMLResponse)
async def get_weather(request: Request, url: str):
    # Your code to fetch weather information from the URL goes here
    response = requests.get(url)
    html = response.text
    beautiful_soup = BeautifulSoup(html, "html.parser")
    temperature = beautiful_soup.find("span", {"class": "temp__value temp__value_with-unit"}).text
    weather_condition = beautiful_soup.find("div", {"class": "link__condition day-anchor i-bem"}).text
    feels_like = beautiful_soup.find("span", {"class": "temp__value temp__value_with-unit"}).text

    context = {"request": request, "temperature": temperature, "weather_condition": weather_condition,
               "feels_like": feels_like}
    return templates.TemplateResponse("weather.html", context=context)
