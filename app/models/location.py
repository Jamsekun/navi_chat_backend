from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, DECIMAL
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ARRAY
from geoalchemy2 import Geometry
from app.core.database import Base

class Building(Base):
    __tablename__ = "buildings"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    code = Column(String(50), unique=True)
    description = Column(Text)
    category = Column(String(100))
    geometry = Column(Geometry('POLYGON', srid=4326), nullable=False)
    entrance_point = Column(Geometry('POINT', srid=4326))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Room(Base):
    __tablename__ = "rooms"
    
    id = Column(Integer, primary_key=True, index=True)
    building_id = Column(Integer, ForeignKey("buildings.id"))
    name = Column(String(255), nullable=False)
    room_number = Column(String(50))
    floor = Column(Integer)
    category = Column(String(100))
    geometry = Column(Geometry('POLYGON', srid=4326))
    center_point = Column(Geometry('POINT', srid=4326), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Path(Base):
    __tablename__ = "paths"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    start_point = Column(Geometry('POINT', srid=4326), nullable=False)
    end_point = Column(Geometry('POINT', srid=4326), nullable=False)
    path_geometry = Column(Geometry('LINESTRING', srid=4326), nullable=False)
    distance_meters = Column(DECIMAL(10, 2))
    accessibility_features = Column(ARRAY(String))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    icon_name = Column(String(100))
    color = Column(String(7))
