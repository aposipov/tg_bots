from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

# from g4f_bot.core_bot.utils.add_user import add_user
from utils.add_user import add_user

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    add_user(message)
    await message.answer(text=
                         "Доброго времени суток!\n"
                         "Если будут вопросы наберите /help")
