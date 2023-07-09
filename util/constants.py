import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN") 
URL = "https://api.exchangerate-api.com/v4/latest/RUB"