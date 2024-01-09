import sqlite3

db_path = '../data/dev_g4f.db'


def init_db():
	db = sqlite3.connect(db_path)
	c = db.cursor()
	try:
		c.execute("CREATE TABLE IF NOT EXISTS g4fusers ("
		          "user_id INTEGER PRIMARY KEY UNIQUE NOT NULL,"
		          "username TEXT NOT NULL,"
		          "full_name TEXT,"
		          "lang VARCHAR,"
		          "date TIMESTAMP)")
	except Exception as e:
		print(f'INIT DB ERROR! {e}')
	db.commit()
	db.close()


init_db()
