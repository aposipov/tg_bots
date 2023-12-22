
# from g4f_bot.core_bot.config import ADMIN_ID
from config import ADMIN_ID

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter, CommandObject
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
# from aiogram.fsm.storage.memory import MemoryStorage
# from g4f_bot.core_bot.main import bot
from main import bot

router = Router()


class Report(StatesGroup):
    fill_report = State()


@router.message(Command(commands='cancel'))
async def cmd_report(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.reply("Отменено! Можете продолжать задавать вопросы!")


@router.message(Command(commands='help'))
async def cmd_help(message: Message) -> None:
    text = "/start - запуск бота\n" \
           "/report - задать вопрос\n" \
           "/cancel - отменить обращение\n" \
           "/restart - очистить историю диалога\n" \
           "/about - о боте"
    await message.answer(text)


@router.message(Command(commands='report'))
async def cmd_report(message: Message, state: FSMContext) -> None:
    await state.set_state(Report.fill_report)
    await message.answer("Напишите вашу проблему")
    # await message.reply("Спасибо")


# @router.message(StateFilter(Report.fill_report))
@router.message(Report.fill_report)
async def fsm_report(message: Message, state: FSMContext) -> None:
    report = message.text
    if len(report) < 9:
        await message.answer("Слишком мало символов, опишите вашу проблему! "
                             "Или отмените /cancel")
    else:
        # await message.answer(report)
        await bot.send_message(chat_id=ADMIN_ID,
                               text='report:\n' +
                                    report + '\n' + 'username: ' +
                                    '@' + message.from_user.username)
        await message.answer("Благодарим за ваше обращение!")
        await state.clear()


@router.message(Command(commands='support'))
async def cmd_report(message: Message, command: CommandObject) -> None:
    input_text = command.args
    print(message.from_user.username, message.chat.id)
    if command.args is None:
        await message.answer("Напишите ваше обращение сразу после команды "
                             "/support после нажмите отправить")
    else:
        await bot.send_message(chat_id=ADMIN_ID,
                               text='Текст сообщения:\n' +
                                    input_text + '\n' +
                                    '@' + message.from_user.username)
        await message.answer("Спасибо за обращение!")


@router.message(Command(commands='about'))
async def cmd_report(message: Message) -> None:
    await message.reply("Я - твой личный AI-ассистент! "
                        "Я здесь, чтобы помочь тебе с информацией, "
                        "заданиями и просто быть твоим виртуальным помощником!")
