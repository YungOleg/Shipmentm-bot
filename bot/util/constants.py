from os import getenv
from dotenv import load_dotenv
from typing import Final
from sqlalchemy import URL

load_dotenv()

TOKEN: Final = getenv("TOKEN") 
ADMIN_ID: Final = getenv("ADMIN_ID")
# URL: Final = getenv("URL")

POSTGRESQL_URL: Final = getenv("POSTGRES_URL")