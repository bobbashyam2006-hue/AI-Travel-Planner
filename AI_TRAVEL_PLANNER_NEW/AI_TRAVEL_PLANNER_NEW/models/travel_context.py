from typing import List, Dict
from pydantic import BaseModel, Field

class TravelInput(BaseModel):
    destination: str
    number_of_days: int
    budget: float
    number_of_travelers: int
    preferences: str
    travel_date: str

class DestinationReport(BaseModel):
    destination: str
    summary: str
    attractions: List[str] = Field(default_factory=list)

class WeatherReport(BaseModel):
    destination: str
    summary: str
    daily: List[Dict] = Field(default_factory=list)

class PlacesReport(BaseModel):
    restaurants: List[str] = Field(default_factory=list)
    activities: List[str] = Field(default_factory=list)

class FinalTravelPlan(BaseModel):
    itinerary: List[Dict] = Field(default_factory=list)
    budget_breakdown: Dict[str, float] = Field(default_factory=dict)
    total_estimated_cost: float = 0
    budget_remaining: float = 0
    budget_status: str = ''
    travel_tips: List[str] = Field(default_factory=list)
