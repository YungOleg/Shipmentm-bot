import aiohttp
import json
from typing import Optional, Dict
from util.constants import URL
from log_config import log
from aiocron import crontab

BASE_URL: str = "https://v6.exchangerate-api.com/v6/55724baadd24ca534b203d88/latest/RUB"
PERCENT: int = 10

# @crontab('0 0 */24 * *')
async def parse_rub() -> Optional[Dict[str, float]]:
    ...


async def make_request(url: str)-> Optional[Dict]:
    ...


async def calculate():
    ...