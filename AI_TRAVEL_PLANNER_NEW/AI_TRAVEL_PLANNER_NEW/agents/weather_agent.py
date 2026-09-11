from utils.geocode_api import geocode_location
from utils.weather_api import get_weather

def run_weather_agent(destination, travel_date, number_of_days):
    try:
        location = geocode_location(destination)
        weather = get_weather(location['latitude'], location['longitude'], travel_date, number_of_days)
        return {'destination': destination, 'summary': weather['summary'], 'daily': weather['daily']}
    except Exception as e:
        return {'destination': destination, 'summary': f'Weather unavailable: {e}', 'daily': []}
