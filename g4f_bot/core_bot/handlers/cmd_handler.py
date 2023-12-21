from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
# from aiogram.fsm.storage.memory import MemoryStorage

router = Router()


@router.message(Command(commands='help'))
async def cmd_help(message: Message) -> None:
    text = "/start - lunch bot\n\
/report - write report\n\
/clear - clear context"
    await message.answer(text)


@router.message(Command(commands='report'))
async def cmd_report(message: Message) -> None:
    await message.answer("Напишите вашу проблему")
    # FSM
    await message.reply("Спасибо")
