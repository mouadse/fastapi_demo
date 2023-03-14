import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()


@app.get("/weather")
def get_weather(url: str):
    # Your code to fetch weather information from the URL goes here
    response = requests.get(url)
    html = response.text
    beautiful_soup = BeautifulSoup(html, "html.parser")
    temperature = beautiful_soup.find("span", {"class": "temp__value temp__value_with-unit"}).text
    weather_condition = beautiful_soup.find("span", {"class": "temp__value temp__value_with-unit"}).text


    pass
