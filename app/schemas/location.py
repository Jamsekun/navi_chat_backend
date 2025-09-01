from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class LocationSearch(BaseModel):
    query: str
    category: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    radius: Optional[float] = 1000

class LocationResponse(BaseModel):
    id: int
    name: str
    type: str
    category: Optional[str]
    coordinates: Dict[str, float]
    distance: Optional[float] = None
    
    class Config:
        from_attributes = True

class RouteRequest(BaseModel):
    start_location: str
    end_location: str
    user_id: Optional[int] = None

class RouteResponse(BaseModel):
    route_id: str
    start_location: str
    end_location: str
    distance: float
    estimated_time: int
    path: List[Dict[str, float]]
    instructions: List[str]
    
    class Config:
        from_attributes = True
