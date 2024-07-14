
from sqlalchemy import create_engine  # for connecting to DB
from sqlalchemy.ext.declarative import declarative_base  # for ORM mappings
from sqlalchemy.orm import sessionmaker  # handles database sessions
from config import Database

db = Database()

# Path to our postgreSQL DB
DATABASE_URL = db.connection_string

# Create a connection engine to the database
engine = create_engine(url=DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(
    autocommit=False,  # transactions will not be committed automatically
    autoflush=False,  # changes will not be flushed to the database automatically
    bind=engine  # associates this session with the engine created above
)

# Base class for our ORM models
Base = declarative_base()
