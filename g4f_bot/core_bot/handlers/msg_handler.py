from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import g4f

router = Router()

# Словарь для хранения истории разговоров
conversation_history = {}


# Функция для обрезки истории разговора
def trim_history(history, max_length=4096):
    current_length = sum(len(message["content"]) for message in history)
    while history and current_length > max_length:
        removed_message = history.pop(0)
        current_length -= len(removed_message["content"])
    return history


@router.message(Command(commands="restart"))
async def process_clear_command(message: Message):
    user_id = message.from_user.id
    conversation_history[user_id] = []
    await message.reply("Контекст истории диалога очищен.")


@router.message()
async def send_welcome(message: Message):
    from g4f_bot.core_bot.main import bot
    # print(message)
    # print(message.from_user.id)
    user_id = message.from_user.id
    user_input = message.text

    if user_id not in conversation_history:
        conversation_history[user_id] = []

    conversation_history[user_id].append({"role": "user", "content": user_input})
    conversation_history[user_id] = trim_history(conversation_history[user_id])

    chat_history = conversation_history[user_id]

    await message.reply("Собираю данные! Готовлю ответ!")
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=chat_history,
            provider=g4f.Provider.GeekGpt,
            # provider=g4f.Provider.ChatBase,
        )
        chat_gpt_response = response
    except Exception as e:
        print(f"{g4f.Provider.GeekGpt.__name__}:", e)
        chat_gpt_response = "Упс, что-то пошло не так. " \
                            "Попробуйте еще раз! Или напишите запрос иначе!"

    conversation_history[user_id].append({"role": "assistant", "content": chat_gpt_response})
    print(conversation_history)
    length = sum(len(message["content"]) for message in conversation_history[user_id])
    print(length)
    # await bot.edit_message_text("SOME TEXT", chat_id=message.chat.id, message_id=message.message_id)
    await message.answer(chat_gpt_response)
