from os import getenv
from dotenv import load_dotenv
from typing import Final

load_dotenv()

TOKEN: Final = getenv("TOKEN") 
ADMIN_ID: Final = getenv("ADMIN_ID")
URL: Final = getenv("URL")

DRIVER_NAME: Final = "postgresql+asyncpg"
DB_HOST: Final = "localhost"
DB_USER: Final = getenv("DB_USER")
DB_PASSWORD: Final = getenv("DB_PASSWORD")
DB_NAME: Final = getenv("DB_NAME")
DB_PORT: Final = getenv("DB_PORT")