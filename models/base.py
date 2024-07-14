
from sqlalchemy import create_engine  # for connecting to DB
from sqlalchemy.ext.declarative import declarative_base  # for ORM mappings
from sqlalchemy.orm import sessionmaker  # handles database sessions

# Path to our SQLite database
DATABASE_URL = "sqlite:///./app/database/PST.db"

# Create a connection engine to the database
# connect_args={"check_same_thread": False} is required for SQLite to allow multiple threads to interact with the database
engine = create_engine(
    url=DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a configured "Session" class
SessionLocal = sessionmaker(
    autocommit=False,  # transactions will not be committed automatically
    autoflush=False,  # changes will not be flushed to the database automatically
    bind=engine  # associates this session with the engine created above
)

# Base class for our ORM models
Base = declarative_base()
