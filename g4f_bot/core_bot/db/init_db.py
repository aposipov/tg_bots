import sqlite3

db_path = '../data/dev_g4f.db'


def init_db():
	db = None
	try:
		db = sqlite3.connect(db_path)
		c = db.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS g4fusers ("
		          "id INTEGER PRIMARY KEY AUTOINCREMENT,"
		          "user_id INTEGER UNIQUE NOT NULL,"
		          "username TEXT,"
		          "full_name TEXT,"
		          "phone TEXT,"
		          "lang VARCHAR,"
		          "premium INTEGER DEFAULT 0,"
		          "date TIMESTAMP)")
	except Exception as e:
		print(f'INIT DB ERROR! {e}')
	db.commit()
	db.close()


init_db()
print("DB create!")
