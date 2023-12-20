import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import BOT_TOKEN, ADMIN_ID, cmds, greeting, about
from handlers import start_handler, cmd_handler, msg_handler

# Включите логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


# @dp.message(CommandStart())
# async def cmd_start(message: Message) -> None:
#     await message.answer("Спасибо! Если будут вопросы наберите /help")


async def main():
    dp.include_router(start_handler.router)
    dp.include_router(cmd_handler.router)
    dp.include_router(msg_handler.router)
    logging.info("BOT IS STARTED!")
    await bot.set_my_commands(cmds)
    await bot.set_my_description(greeting)
    await bot.set_my_short_description(about)
    await dp.start_polling(bot)
    logging.info("STOP!")


# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())
