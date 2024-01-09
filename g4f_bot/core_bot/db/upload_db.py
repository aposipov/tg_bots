import csv
import sqlite3

path_to_file = '../data/all.csv'
db_path = '../data/test.db'


def db_add(row):
	user_id: int = row[0]
	username: str = row[1]
	full_name: str = row[2]
	lang: str = row[3]
	date = row[4]
	# print(user_id, username, full_name, lang, date)
	try:
		db = sqlite3.connect(db_path)
		c = db.cursor()
		c.execute("INSERT INTO g4fusers VALUES (?,?,?,?,?)",
		          (user_id, username, full_name, lang, date))
		db.commit()
		db.close()
		print(f'User {user_id} added to DB!')
	except sqlite3.Error as e:
		print(f'add_data ERROR! {e}')


def read_file():
	try:
		with open(path_to_file, 'r', encoding='utf-8') as f:
			reader = csv.reader(f, delimiter=';')
			for row in reader:
				if row and row[0].isdigit():
					db_add(row)
				else:
					continue
	except Exception as e:
		print(f'ERROR {e}')


read_file()
