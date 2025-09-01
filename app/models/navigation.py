from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL, JSON
from sqlalchemy.sql import func
from app.core.database import Base

class Route(Base):
    __tablename__ = "routes"
    
    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(String(255), unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    start_location = Column(String(255), nullable=False)
    end_location = Column(String(255), nullable=False)
    distance = Column(DECIMAL(10, 2))
    estimated_time = Column(Integer)  # in minutes
    path_data = Column(JSON)  # Store route coordinates
    instructions = Column(JSON)  # Store turn-by-turn instructions
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True))

class RoutePoint(Base):
    __tablename__ = "route_points"
    
    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(Integer, ForeignKey("routes.id"))
    sequence = Column(Integer, nullable=False)  # Order in the route
    latitude = Column(DECIMAL(10, 8), nullable=False)
    longitude = Column(DECIMAL(11, 8), nullable=False)
    instruction = Column(String(500))  # Turn-by-turn instruction
    distance_from_start = Column(DECIMAL(10, 2))  # Distance from route start
