import requests

def geocode_location(location):
    response = requests.get('https://geocoding-api.open-meteo.com/v1/search', params={'name': location, 'count': 1, 'language': 'en', 'format': 'json'}, timeout=30)
    response.raise_for_status()
    results = response.json().get('results', [])
    if not results: raise ValueError(f'Location not found: {location}')
    r = results[0]
    return {'latitude': r['latitude'], 'longitude': r['longitude'], 'resolved_address': ', '.join(x for x in [r.get('name'), r.get('admin1'), r.get('country')] if x)}
