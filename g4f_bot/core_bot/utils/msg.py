import sqlite3
from db.requests import db_path


async def get_uid(uname: str):
	# print("get_uid")
	# print(uname)
	# print(uname[0])
	try:
		db = sqlite3.connect(db_path)
		c = db.cursor()
		c.execute("SELECT user_id FROM g4fusers WHERE username = ?", (uname,))
		uid = c.fetchone()
		# print("get_uid")
		# print(uid)
		return uid[0]
	except sqlite3.Error as e:
		print(f'get_uid ERROR! {e}')
		return None


async def msg(uname: str, text: str):
	from main import bot
	if uname.isdigit():
		await bot.send_message(chat_id=uname, text=text)
	else:
		uid = await get_uid(uname)
		await bot.send_message(chat_id=uid, text=text)
