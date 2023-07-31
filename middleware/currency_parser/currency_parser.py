import aiohttp
import json
from typing import Optional, Dict
from util.constants import URL
from log_config import log
from aiocron import crontab


@crontab('0 0 */24 * *') 
async def parse_rub() -> Optional[Dict[str, float]]:
    """
        Функция для парсинга курса валют(доллар и евро), выполняется 1 раз в день
    """
    data = await make_request(URL)
    if data is not None:
        usd = format(1 / float(json.dumps(data["rates"]["USD"])), ".2f")
        eur = format(1 / float(json.dumps(data["rates"]["EUR"])), ".2f")
        log.info("Request successful")
        return {"usd" : usd, "eur": eur}
    return None


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