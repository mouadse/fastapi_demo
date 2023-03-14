# Weather Information Application

This is a simple web application that allows you to get the current weather information from a specified website. The
application is built using Python and FastAPI framework, and it uses Beautiful Soup to extract data from HTML.

## Requirements

To run this application, you need to have the following software installed on your computer:

- Python 3.7 or higher
- FastAPI
- Requests
- Beautifulsoup
- Jinja2

## Installation

To install the required packages, run the following command:
> **pip install fastapi requests beautifulsoup4 jinja2**

## Usage

To run the application, navigate to the directory where the main.py file is located and run the following command:
> **uvicorn main:app --reload**

Once the server is running, you can access the application by opening your web browser and navigating
to http://localhost:8000/weather?url=URL_OF_WEBSITE. Replace URL_OF_WEBSITE with the URL of the website you want to
fetch weather information from.

## How It Works

The application takes a URL as input and extracts weather information from the specified website using Beautiful Soup.
The temperature, weather condition, and feels-like temperature are then displayed in a simple, elegant HTML page.

