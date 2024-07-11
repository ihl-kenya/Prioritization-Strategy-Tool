from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

# Database classes that interact with the database will be defined here


class User(Base):
    """Users table will be defined here and its attributes"""


class Product(Base):
    """Products Table and its attributes """


class Facility(Base):
    """Facilities table"""


class Forecast(Base):
    """Forecasts table and its attributes """
