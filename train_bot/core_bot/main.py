from config.config import BOT_TOKEN
import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, BotCommand
from add_user import add_user

dp = Dispatcher()

cmds = [
	BotCommand(command="start", description="start bot"),
	BotCommand(command="report", description="Report message to group admins"),
	BotCommand(command="admin", description="check admin"),
]


@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
	add_user(message.from_user.full_name, message.from_user.id, message.from_user.username)
	print(message.from_user.full_name, message.from_user.id, message.from_user.username)
	print(message.from_user.is_bot)
	print(message.from_user.language_code)
	print(message.from_user.is_premium)
	print(message.date)
	# print(message.reply_location())
	# print(message.answer_location())
	await message.reply("Hello")


async def main():
	bot = Bot(BOT_TOKEN)
	await bot.set_my_commands(cmds)
	await dp.start_polling(bot)


if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)
	asyncio.run(main())
