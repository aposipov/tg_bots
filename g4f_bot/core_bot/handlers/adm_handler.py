from config import ADMIN_ID
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from utils.shout import shout
from db.requests import get_uname
import csv

router = Router()


# async def shout_list(text: str):
# 	from main import bot
# 	path_to_file = './data/users.csv'
# 	with open(path_to_file, 'r', encoding='utf-8') as f:
# 		reader = csv.reader(f, delimiter=';')
# 		for line in reader:
# 			if line and line[0].isdigit() and text:
# 				print(line[0])
# 				await bot.send_message(chat_id=line[0],
# 				                 text=text)
# 			else:
# 				continue


@router.message(Command(commands='adm'))
async def shout_handler(message: Message):
	if str(message.from_user.id) != ADMIN_ID:
		await message.answer("⚠️ FATAL ERROR! ⚠️")
	else:
		await message.answer("⚠️\n "
		                     "/shout\n"
		                     "/unames ")


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


@router.message(Command(commands='unames'))
async def uname_handler(message: Message):
	unames = str(get_uname())
	await message.answer(unames)
