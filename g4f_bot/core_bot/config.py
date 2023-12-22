from environs import Env
from aiogram.types import BotCommand

env = Env()
env.read_env()
BOT_TOKEN = env.str("TOKEN")
ADMIN_ID = env.str("ADMIN_ID")

# при перезапуске команды обновляются
cmds = [
	BotCommand(command="start", description="запуск бота"),
	BotCommand(command="help", description="помощь"),
	BotCommand(command="restart", description="очистить историю"),
	BotCommand(command="report", description="задать вопрос"),
	BotCommand(command="cancel", description="отменить обращение в поддержку"),
	# BotCommand(command="support", description="написать в поддержку"),
	BotCommand(command="about", description="обо мне"),
]

# bot.set_my_description
greeting = "Я помогу вам с вопросами или написанием текста. " \
           "Старайтесь формулировать свои запросы со слов: " \
           "напиши, объясни, расскажи кратко."

# bot.set_my_short_description
about = "Нейросетевая модель ChatGPT от openAI "\
        "\n"\
        "Умеет отвечать на вопросы, вести диалог, писать код."
