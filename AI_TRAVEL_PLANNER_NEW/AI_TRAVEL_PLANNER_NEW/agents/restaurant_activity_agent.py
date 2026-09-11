from utils.places_api import search_places

def run_restaurant_activity_agent(destination, budget, number_of_travelers, preferences):
    places = search_places(destination)
    return {'restaurants': places.get('restaurants', []), 'activities': places.get('activities', [])}
