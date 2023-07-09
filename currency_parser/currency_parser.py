import aiohttp
import asyncio
import json
import logging
from typing import Optional, Dict
from util.constants import URL



logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


async def make_request(url: str)-> Optional[Dict]:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                return data
    except aiohttp.ClientError as e:
        log.error(f"Request error: {e}")
        return None
    except Exception as e:
        log.error(f"Error: {e}")
        return None


async def parse_rub() -> Optional[Dict[str, float]]:
    data = await make_request(URL)
    if data is not None:
        usd = format(1 / float(json.dumps(data["rates"]["USD"])), ".2f")
        eur = format(1 / float(json.dumps(data["rates"]["EUR"])), ".2f")
        return {"usd" : usd, "eur": eur}
    return None


# async def format_currency(data: Dict, currency: str) -> float:
#     return "{:.2f}".format(1 / float(data["rates"][currency]))