import asyncio

import aiohttp
import json
from typing import Optional, Dict
from pydantic import BaseModel
from aiocron import crontab


class RubleRate(BaseModel):
    cny: float
    usd: float
    eur: float


PATH = r"C:\\Users\\bilk5\\Desktop\Shipmentm-bot\\bot\\util\\currency_parser\\ruble_rate.json"
URL: str = "https://v6.exchangerate-api.com/v6/55724baadd24ca534b203d88/latest/RUB"
PERCENT: int = 10


async def _make_request() -> RubleRate:
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            data = await response.json()
            cny = round(1 / float(data.get("conversion_rates").get("CNY")), 3)
            usd = round(1 / float(data.get("conversion_rates").get("USD")), 3)
            eur = round(1 / float(data.get("conversion_rates").get("EUR")), 3)
            return RubleRate(cny=cny, usd=usd,eur=eur)


@crontab("0 0 * * *") 
async def write_json() -> None:
    data = await _make_request()
    ruble_rate = {
        "cny": data.cny,
        "usd": data.usd,
        "eur": data.eur
        }
    ruble_rate_json = json.dumps(ruble_rate, indent=4)
    with open(PATH, "w") as file:
        file.write(ruble_rate_json)


async def _get_data() -> Dict[str, float]:
    with open(PATH, "r") as file:
        data = json.load(file)
    return data


async def _get_currency(mode: str) -> int:
    data = await _get_data()
    match mode:
        case "usd":
            usd = data.get("usd")
            return usd
        case "cny":
            cny = data.get("cny")
            return cny
        case "eur":
            eur = data.get("eur")
            return eur


async def calculate(amount: float, mode: str, shop_from: str) -> float:
    # TODO: Найти формулу для вычисления доставки
    rate = await _get_currency(mode=mode)
    match shop_from:
        case "poizon":
            price = amount * rate * 1.2
            return price
        case "tradeinn":
            ...
        case "other":
            ...


async def main():
    # python bot\util\currency_parser\currency_parser.py
    ...

asyncio.run(main())