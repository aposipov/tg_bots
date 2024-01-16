from config import ADMIN_ID
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from utils.shout import shout
from utils.msg import msg
from db.requests import get_unames
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class Msguser(StatesGroup):
    fill_msg = State()


@router.message(Command(commands='adm'))
async def shout_handler(message: Message):
	if str(message.from_user.id) != ADMIN_ID:
		await message.answer("⚠️ FATAL ERROR! ⚠️")
	else:
		await message.answer("⚠️ adm commands:\n "
		                     "/shout text message\n"
		                     "/msg @username\n"
		                     "/unames all users")


@router.message(Command(commands='shout'))
async def shout_handler(message: Message, command: CommandObject):
	print(command.args)
	if str(message.from_user.id) != ADMIN_ID:
		await message.answer("⚠️ FATAL ERROR! ⚠️")
	else:
		if command.args is None:
			await message.answer("⚠️ you have admin priviligies!")
		else:
			await shout(command.args)
			await message.answer("✅ msgs was sended!")


@router.message(Command(commands='msg'))
async def msg_handler(message: Message, command: CommandObject, state: FSMContext):
	print(command.args)
	uname = command.args
	if str(message.from_user.id) != ADMIN_ID:
		await message.answer("⚠️ FATAL ERROR! ⚠️")
	else:
		if command.args is None:
			await message.answer("⚠️ you have admin priviligies!")
		else:
			await state.update_data(id=uname)
			await state.set_state(Msguser.fill_msg)


@router.message(Msguser.fill_msg)
async def fsm_msg(message: Message, state: FSMContext) -> None:
	report = message.text
	data = await state.get_data()
	uname = data.get('id')
	# print(command.args)
	print(report)
	# await message.answer(report + '*' + cmd)
	await msg(uname, report)
	await message.answer("✅ msg was sended!")
	await state.clear()


@router.message(Command(commands='unames'))
async def uname_handler(message: Message):
	unames = str(get_unames())
	await message.answer(unames)
