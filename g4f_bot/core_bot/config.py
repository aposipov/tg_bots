from environs import Env
from aiogram.types import BotCommand

env = Env()
env.read_env()
BOT_TOKEN = env.str("TOKEN")
ADMIN_ID = env.str("ADMIN_ID")

# при перезапуске команды обновляются
cmds = [
	BotCommand(command="start", description="text1"),
	BotCommand(command="help", description="text2"),
	BotCommand(command="clear", description="text3"),
	BotCommand(command="report", description="text4"),
]

# bot.set_my_description
greeting = "Description from config!"

# bot.set_my_short_description
about = "About Me! I am BOt!"
