import json
from agents.orchestrator_agent import run_orchestrator

def main():
    print('=' * 60)
    print('AI TRAVEL PLANNING AGENT')
    print('=' * 60)
    destination = input('Destination: ')
    days = int(input('Number of days: '))
    travelers = int(input('Number of travelers: '))
    budget = float(input('Budget (₹): '))
    travel_date = input('Travel start date (YYYY-MM-DD): ')
    preferences = input('Preferences: ')
    result = run_orchestrator(destination, days, budget, travelers, preferences, travel_date)
    print(json.dumps(result, indent=4, ensure_ascii=False))

if __name__ == '__main__': main()
