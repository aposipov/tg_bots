
from aiogram.types import Message
import csv

path_to_file = './data/users.csv'


def add_user(message: Message):
	user_id: int = message.from_user.id

	if message.from_user.username is None:
		username: str = 'null'
	else:
		username = '@' + message.from_user.username

	full_name: str = message.from_user.full_name

	phone: str = 'null'

	lang: str = message.from_user.language_code
	premium: bool = message.from_user.is_premium
	date: str = message.date
	fieldnames: list = [user_id, username, full_name, phone, lang, premium, date]
	try:
		with open(path_to_file, 'a', encoding='utf-8') as f:
			writer = csv.writer(f, delimiter=';')
			writer.writerow(fieldnames)
		print(f"User {user_id} added to file!")
	except Exception as e:
		print(f'Error: {e}')


# add_user()
