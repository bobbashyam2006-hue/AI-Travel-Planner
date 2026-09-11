from utils.geocode_api import geocode_location

def test_geocoding():
    result = geocode_location('Hyderabad')
    assert result['latitude'] is not None
    assert result['longitude'] is not None
