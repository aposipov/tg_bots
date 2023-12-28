import sqlite3


def init_db():
	db = sqlite3.connect('../data/dev_g4f.db')
	c = db.cursor()
	try:
		c.execute("CREATE TABLE IF NOT EXISTS g4fusers ("
		          "user_id INTEGER PRIMARY KEY UNIQUE NOT NULL,"
		          "username TEXT NOT NULL,"
		          "full_name TEXT,"
		          "lang VARCHAR,"
		          "date TIMESTAMP)")
	except Exception as e:
		print(f'DB ERROR! {e}')
	db.commit()
	db.close()


init_db()
