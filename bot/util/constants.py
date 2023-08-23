from os import getenv
from dotenv import load_dotenv
from typing import Final
from sqlalchemy import URL

load_dotenv()

TOKEN: Final = getenv("TOKEN") 
ADMIN_ID: Final = getenv("ADMIN_ID")
# URL: Final = getenv("URL")

DRIVER_NAME: Final = "postgresql+asyncpg"
DB_HOST: Final = "localhost"
DB_USER: Final = getenv("DB_USER")
DB_PASSWORD: Final = getenv("DB_PASSWORD")
DB_NAME: Final = getenv("DB_NAME")
DB_PORT: Final = getenv("DB_PORT")

POSTGRESQL_URL = URL.create(
    drivername=DRIVER_NAME,
    username=DB_USER,
    database=DB_NAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
    )