import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/weather", response_class=HTMLResponse)
def get_weather(url: str):
    # Your code to fetch weather information from the URL goes here
    response = requests.get(url)
    html = response.text
    beautiful_soup = BeautifulSoup(html, "html.parser")
    temperature = beautiful_soup.find("span", {"class": "temp__value temp__value_with-unit"}).text
    weather_condition = beautiful_soup.find("div", {"class": "link__condition day-anchor i-bem"}).text
    feels_like = beautiful_soup.find("span", {"class": "temp__value temp__value_with-unit"}).text
    return """
       <html>
           <head>
               <title>Some HTML in here</title>
           </head>
           <body>
               <h1>Look ma! HTML!</h1>
               <p>Here's some weather information: {{ temperature }}</p>
                <p>Here's some weather information: {{ weather_condition }}</p>
                <p>Here's some weather information: {{ feels_like }}</p>
           </body>
       </html>
       """
