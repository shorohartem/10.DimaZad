from fastapi import APIRouter, Depends

from app.services.binance_crypto import get_binance_service, get_bybit_service
router = APIRouter()

@router.get("/piars")
async def piars(
    binance_service = Depends(get_binance_service),
    bybit_service = Depends(get_bybit_service)
):
    binance_coin = await binance_service.get_pairs()
    bybit_coin = await bybit_service.get_pairs()
    return {
        "binance_coin": binance_coin[:5],
        "bybit_coin": bybit_coin[:5]
    }

@router.get("/checkCoin")
async def checkCoin(
        binance_service = Depends(get_binance_service),

):
    pairs = await binance_service.get_pairs()
    return pairs[:5]


