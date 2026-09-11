from models.travel_context import TravelInput

def test_travel_input():
    item = TravelInput(destination='Goa', number_of_days=3, budget=30000, number_of_travelers=2, preferences='beaches', travel_date='2026-12-01')
    assert item.destination == 'Goa'
    assert item.number_of_days == 3
