import os
from dotenv import load_dotenv
from typing import Final

load_dotenv()

TOKEN: Final = os.getenv("TOKEN") 
ADMIN_ID: Final = os.getenv("ADMIN_ID")
URL: Final = os.getenv("URL")