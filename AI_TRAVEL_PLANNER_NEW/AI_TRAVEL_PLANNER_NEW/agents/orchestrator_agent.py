from agents.destination_research_agent import run_destination_research_agent
from agents.weather_agent import run_weather_agent
from agents.restaurant_activity_agent import run_restaurant_activity_agent
from agents.itinerary_budget_agent import run_itinerary_budget_agent

def run_orchestrator(destination, number_of_days, budget, number_of_travelers, preferences, travel_date):
    print('[1/4] Destination Research Agent')
    research = run_destination_research_agent(destination, number_of_days, preferences)
    print('[2/4] Weather Agent')
    weather = run_weather_agent(destination, travel_date, number_of_days)
    print('[3/4] Restaurant & Activity Agent')
    places = run_restaurant_activity_agent(destination, budget, number_of_travelers, preferences)
    print('[4/4] Itinerary & Budget Agent')
    final_plan = run_itinerary_budget_agent(destination, number_of_days, budget, number_of_travelers, preferences, research, weather, places)
    return {'input': {'destination': destination, 'number_of_days': number_of_days, 'budget': budget, 'number_of_travelers': number_of_travelers, 'preferences': preferences, 'travel_date': travel_date}, 'destination_research': research, 'weather': weather, 'places': places, 'final_plan': final_plan}
