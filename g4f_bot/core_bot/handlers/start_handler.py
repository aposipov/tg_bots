from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from utils.add_user import add_user
from db.requests import add_data

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    add_user(message)
    add_data(message)
    await message.answer(text=
                         "Доброго времени суток!\n"
                         "Если будут вопросы наберите /help")
