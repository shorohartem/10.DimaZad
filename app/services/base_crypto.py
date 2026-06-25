from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class CoinValue:
    symbol: str
    price: float

class BaseCryptoProvider():
    @abstractmethod
    async def get_coin(self, coin_name: str) -> CoinValue:
        pass

    @abstractmethod
    async def get_pairs(self) -> list[CoinValue]:
        pass