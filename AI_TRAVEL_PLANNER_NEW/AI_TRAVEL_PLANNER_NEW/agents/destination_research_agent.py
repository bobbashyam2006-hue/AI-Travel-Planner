from utils.ollama_client import ask_ollama_json

def run_destination_research_agent(destination, number_of_days, preferences):
    prompt = f'''You are a Destination Research Agent. Destination: {destination}. Trip length: {number_of_days} days. Preferences: {preferences}. Recommend 8 important attractions suitable for the traveler. Return ONLY valid JSON: {{"summary":"short useful destination summary","attractions":["attraction 1","attraction 2","attraction 3","attraction 4","attraction 5","attraction 6","attraction 7","attraction 8"]}}'''
    try:
        result = ask_ollama_json(prompt)
        return {'destination': destination, 'summary': result.get('summary', ''), 'attractions': result.get('attractions', [])}
    except Exception as e:
        return {'destination': destination, 'summary': f'Research agent fallback for {destination}.', 'attractions': [], 'error': str(e)}
