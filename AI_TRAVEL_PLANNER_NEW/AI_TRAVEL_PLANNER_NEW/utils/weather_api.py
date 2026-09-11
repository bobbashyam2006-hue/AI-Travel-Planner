import requests
from datetime import date, timedelta

def get_weather(latitude, longitude, start_date, number_of_days):
    start = date.fromisoformat(start_date)
    end = start + timedelta(days=number_of_days - 1)
    response = requests.get('https://api.open-meteo.com/v1/forecast', params={'latitude': latitude, 'longitude': longitude, 'daily': 'temperature_2m_max,temperature_2m_min,precipitation_probability_max,weathercode', 'start_date': start.isoformat(), 'end_date': end.isoformat(), 'timezone': 'auto'}, timeout=30)
    response.raise_for_status()
    daily = response.json().get('daily', {})
    result = []
    for i, current_date in enumerate(daily.get('time', [])):
        minimum = daily['temperature_2m_min'][i]; maximum = daily['temperature_2m_max'][i]; rain = daily['precipitation_probability_max'][i]
        result.append({'date': current_date, 'min_temp_c': minimum, 'max_temp_c': maximum, 'rain_probability': rain, 'description': f'{minimum}°C to {maximum}°C; rain probability {rain}%'})
    return {'summary': f'Weather forecast retrieved for {len(result)} day(s).', 'daily': result}
