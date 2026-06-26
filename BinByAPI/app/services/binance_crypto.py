import aiohttp
import asyncio

from app.services.base_crypto import BaseCryptoProvider, CoinValue


class BinanceProvider(BaseCryptoProvider):
    def __init__(self):
        self.url = "https://api.binance.com/api/v3/ticker/price"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Content-Type": "application/json",
        }

    async def get_pairs(self) -> list[CoinValue]:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url, headers=self.headers) as response:
                    data = await response.json()
                    lst_pairs = [CoinValue(symbol=item["symbol"], price=float(item["price"]))
                                 for item in data]
                    return lst_pairs
        except Exception as e:
            print(f'Произошла ошибка при запросе к Binance: {e}')
            return []




class BybitProvider(BaseCryptoProvider):
    def __init__(self):
        self.url = "https://api.bybit.com/v5/market/tickers"
        self.params = {"category":'spot'}

    async def get_pairs(self) -> list[CoinValue]:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url, params=self.params) as response:

                    response.raise_for_status()

                    data = await response.json()

                    return[
                        CoinValue(symbol=item["symbol"],
                                price=float(item["lastPrice"]))
                        for item in data["result"]["list"]]
        except Exception as e:
            print(f'Произошла ошибка при запросе к ByBit: {e}')
            return []

async def get_binance_service() -> BaseCryptoProvider:
    return BinanceProvider()

async def get_bybit_service() -> BybitProvider:
    return BybitProvider()
