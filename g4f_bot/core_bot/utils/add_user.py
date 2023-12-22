
from aiogram.types import Message
import csv

path_to_file = './data/users.csv'


# def add_user():
def add_user(message: Message):
	user_id: str = message.from_user.id
	username: str = '@' + message.from_user.username
	full_name: str = message.from_user.full_name
	# bot_id =
	lang: str = message.from_user.language_code
	date: str = message.date
	fieldnames: list = [user_id, username, full_name, lang, date]
	# test_list = ['user_id', 'username', 'full_name', 'lang']
	try:
		with open(path_to_file, 'a', encoding='utf-8') as f:
			writer = csv.writer(f, delimiter=';')
			writer.writerow(fieldnames)
		print(f"User {user_id} added to file!")
	except Exception as e:
		print(f'Error: {e}')


# add_user()
