from utils.ollama_client import ask_ollama_json

def run_itinerary_budget_agent(destination, days, budget, travelers, preferences, research, weather, places):
    prompt = f'''You are the Final Itinerary and Budget Agent. Destination: {destination}. Days: {days}. Travelers: {travelers}. Budget: ₹{budget}. Preferences: {preferences}. Attractions: {research.get('attractions', [])}. Weather: {weather.get('daily', [])}. Restaurants: {places.get('restaurants', [])}. Activities: {places.get('activities', [])}. Create a practical itinerary with exactly {days} days and estimate costs realistically. Return ONLY valid JSON: {{"itinerary":[{{"day":1,"morning":"...","afternoon":"...","evening":"..."}}],"budget_breakdown":{{"accommodation":0,"food":0,"transport":0,"activities":0,"miscellaneous":0}},"total_estimated_cost":0,"budget_remaining":0,"budget_status":"Within budget","travel_tips":["tip 1","tip 2","tip 3"]}}'''
    try:
        result = ask_ollama_json(prompt)
    except Exception:
        parts = {'accommodation': budget*.35, 'food': budget*.20, 'transport': budget*.20, 'activities': budget*.15, 'miscellaneous': budget*.10}
        result = {'itinerary': [{'day': d, 'morning': 'Visit a major attraction.', 'afternoon': 'Lunch and local sightseeing.', 'evening': 'Explore the local area and relax.'} for d in range(1, days+1)], 'budget_breakdown': parts, 'total_estimated_cost': budget, 'travel_remaining': 0, 'budget_status': 'Estimated fallback budget', 'travel_tips': ['Check attraction opening hours.', 'Keep an indoor backup plan for bad weather.', 'Confirm prices before booking.']}
    breakdown = {}
    for key, value in result.get('budget_breakdown', {}).items():
        try: breakdown[key] = float(value)
        except (TypeError, ValueError): breakdown[key] = 0.0
    total = sum(breakdown.values())
    try: total = float(result.get('total_estimated_cost', total))
    except (TypeError, ValueError): pass
    result['budget_breakdown'] = breakdown
    result['total_estimated_cost'] = round(total, 2)
    result['budget_remaining'] = round(float(budget) - total, 2)
    result['budget_status'] = 'Within budget' if total <= budget else 'Over budget'
    result.setdefault('itinerary', [])
    result.setdefault('travel_tips', [])
    return result
