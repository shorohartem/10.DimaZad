import sys
from pathlib import Path

# Добавляем пути ДО всех импортов
sys.path.insert(0, r'C:\Users\user\Desktop\ITMentor\10.DimaZad\BinByAPI')
sys.path.insert(0, str(Path(__file__).parent))

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
from app.services.binance_crypto import BinanceProvider

BOT_TOKEN = '8659040665:AAFb0Szd2HQ9FPc3xlb3ZoRWk5EHmEHFROw'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



@dp.message(Command('start'))
async def start(message: Message):
    await message.answer("Введи /checkCoin чтобы посмотреть список и цену монет.")


@dp.message(Command('checkCoin'))
async def check_coin(message: Message):
    provider = BinanceProvider()
    pairs = await provider.get_pairs()

    if not pairs:
        await message.answer("Не удалось получить данные с Binance")
        return

    text = 'Топ-5 монет с Binance:\n\n'
    for coin in pairs[:5]:
        text += f" {coin.symbol}: {coin.price}$\n"

    await message.answer(text)


if __name__ == '__main__':
    asyncio.run(main())
    print("Bot started.")