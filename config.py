import os
from dotenv import load_dotenv


load_dotenv()


class Database:
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_PORT = os.getenv("DB_PORT")

    connection_string = f"postgresql://{DB_HOST}/{
        DB_NAME}?user={DB_USERNAME}&password={DB_PASSWORD}"
