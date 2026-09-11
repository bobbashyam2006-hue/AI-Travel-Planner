import requests
OVERPASS_URL = 'https://overpass-api.de/api/interpreter'

def search_places(destination):
    from utils.geocode_api import geocode_location
    geo = geocode_location(destination)
    lat, lon = geo['latitude'], geo['longitude']
    query = f'''[out:json][timeout:25];(nwr(around:8000,{lat},{lon})["amenity"="restaurant"];nwr(around:8000,{lat},{lon})["tourism"="attraction"];nwr(around:8000,{lat},{lon})["leisure"="park"];);out center tags;'''
    try:
        response = requests.post(OVERPASS_URL, data=query, timeout=45)
        response.raise_for_status()
        elements = response.json().get('elements', [])
    except Exception:
        return {'restaurants': [], 'activities': []}
    restaurants, activities = [], []
    for element in elements:
        tags = element.get('tags', {}); name = tags.get('name')
        if not name: continue
        if tags.get('amenity') == 'restaurant':
            if name not in restaurants: restaurants.append(name)
        elif name not in activities: activities.append(name)
    return {'restaurants': restaurants[:10], 'activities': activities[:15]}
