import re
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")


def is_valid_meteum_link(link):
    pattern = re.compile(r'^https?://(?:www\.)?meteum\.ai(?:/\S+)?$')
    match = pattern.match(link)
    if match:
        return True
    else:
        return False


@app.get("/weather", response_class=HTMLResponse)
async def get_weather(request: Request, url: str):
    if not is_valid_meteum_link(url):
        return "Invalid URL provided. Please provide a valid URL for https://meteum.ai/."

    response = requests.get(url)
    html = response.text
    beautiful_soup = BeautifulSoup(html, "html.parser")
    temperature = beautiful_soup.find("span", {"class": "temp__value temp__value_with-unit"}).text
    weather_condition = beautiful_soup.find("div", {"class": "link__condition day-anchor i-bem"}).text
    feels_like = beautiful_soup.find("span", {"class": "temp__value temp__value_with-unit"}).text

    context = {"request": request, "temperature": temperature, "weather_condition": weather_condition,
               "feels_like": feels_like}
    return templates.TemplateResponse("weather.html", context=context)

"""
This
is
a
multi-line
comment
to
balance
the
amount
of  
html
and
python
code
in
the
project
"""
