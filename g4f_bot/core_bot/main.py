# https://github.com/xtekky/gpt4free

import logging
import asyncio
import sys
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN, cmds, greeting, about
from handlers import start_handler, cmd_handler, media_handler, adm_handler, msg_handler

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


async def main():
    # bot = Bot(BOT_TOKEN)
    # dp = Dispatcher()
    await adm_handler.shout_list("Мой сервер был перезапущен! 😵‍💫🙃 "
                                 "Ваш контекст истории диалога очищен! "
                                 "Если не хотите получать такие оповещения напишите сюда /report")
    dp.include_router(start_handler.router)
    dp.include_router(cmd_handler.router)
    # add picture and audio handler
    dp.include_router(media_handler.router)
    dp.include_router(adm_handler.router)
    dp.include_router(msg_handler.router)
    logging.info("BOT IS STARTED!")
    await bot.set_my_commands(cmds)
    await bot.set_my_description(greeting)
    await bot.set_my_short_description(about)
    await dp.start_polling(bot)
    logging.info("STOP!")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout,
                        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")
