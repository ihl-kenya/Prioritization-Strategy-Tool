from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

# Database tables will be declared here


class User(Base):
    """Users table will be defined here and its attributes"""


class Product(Base):
    """Products Table and its attributes """


class Facility(Base):
    """Facilities table"""


class Forecast(Base):
    """Forecasts table and its attributes """
