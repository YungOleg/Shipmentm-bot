from os import getenv
from dotenv import load_dotenv
from typing import Final

load_dotenv()

TOKEN: Final = getenv("TOKEN") 
ADMIN_ID: Final = getenv("ADMIN_ID")
POSTGRESQL_URL: Final = getenv("POSTGRES_URL")
