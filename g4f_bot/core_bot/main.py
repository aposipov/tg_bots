import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import g4f
from config import BOT_TOKEN, ADMIN_ID, cmds, greeting, about
from handlers import cmd_handler, msg_handler

# Включите логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


# Словарь для хранения истории разговоров
# conversation_history = {}

# Функция для обрезки истории разговора
# def trim_history(history, max_length=4096):
#     current_length = sum(len(message["content"]) for message in history)
#     while history and current_length > max_length:
#         removed_message = history.pop(0)
#         current_length -= len(removed_message["content"])
#     return history


@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer("Спасибо! Если будут вопросы наберите /help")


# @dp.message(Command("help"))
# async def cmd_help(message: Message) -> None:
#     text = "/start - lunch bot\n\
# /report - write report\n\
# /clear - clear context"
#     await message.answer(text)


# @dp.message(Command("report"))
# async def cmd_report(message: Message) -> None:
#     await message.answer("Напишите вашу проблему")
#     await message.reply("Спасибо")


# @dp.message(Command("clear"))
# async def process_clear_command(message: Message):
#     user_id = message.from_user.id
#     conversation_history[user_id] = []
#     await message.reply("История диалога очищена.")


# Обработчик для каждого нового сообщения
# @dp.message()
# async def send_welcome(message: Message):
#     print(message)
#     print(message.from_user.id)
#     user_id = message.from_user.id
#     user_input = message.text
#
#     if user_id not in conversation_history:
#         conversation_history[user_id] = []
#
#     conversation_history[user_id].append({"role": "user", "content": user_input})
#     conversation_history[user_id] = trim_history(conversation_history[user_id])
#
#     chat_history = conversation_history[user_id]
#
#     try:
#         response = await g4f.ChatCompletion.create_async(
#             model=g4f.models.default,
#             messages=chat_history,
#             provider=g4f.Provider.GeekGpt,
#         )
#         chat_gpt_response = response
#     except Exception as e:
#         print(f"{g4f.Provider.GeekGpt.__name__}:", e)
#         chat_gpt_response = "Упс, что-то пошло не так. Попробуйте еще раз! \
# Или напишите запрос иначе!"
#
#     conversation_history[user_id].append({"role": "assistant", "content": chat_gpt_response})
#     print(conversation_history)
#     length = sum(len(message["content"]) for message in conversation_history[user_id])
#     print(length)
#     await message.answer(chat_gpt_response)


async def main():
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
