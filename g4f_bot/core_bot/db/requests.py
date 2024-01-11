import asyncio
import aiosqlite
import sqlite3
from aiogram.types import Message


# async def add_data():
#     try:
#         async with aiosqlite.connect('../data/dev_g4f.db') as db:
#             async with db.cursor() as cursor:
#                 await cursor.execute("INSERT INTO g4fbotdb VALUES "
#                                      "('1123123', 'fdg', 'apos', 'fdjksfhkjsdhf')")
#             await db.commit()
#     except Exception as e:
#         print(f"Error inserting data into the database: {e}")

db_path = 'data/dev_g4f.db'


def add_data(message: Message):
    user_id: int = message.from_user.id
    if message.from_user.username is None:
        username: str = 'null'
    else:
        username = '@' + message.from_user.username
    full_name: str = message.from_user.full_name
    phone: str = 'null'
    lang: str = message.from_user.language_code
    premium: bool = message.from_user.is_premium
    date = message.date
    db = None
    try:
        db = sqlite3.connect(db_path)
        c = db.cursor()
        c.execute("INSERT INTO g4fusers VALUES (NULL,?,?,?,?,?,?,?)",
                  (user_id, username, full_name, phone, lang, premium, date))
        db.commit()
        db.close()
        print(f'User {user_id} added to DB!')
    except sqlite3.Error as e:
        print(f'add_data ERROR! {e}')
    finally:
        if db:
            db.close()


def get_uids() -> list:
    db = None
    try:
        db = sqlite3.connect(db_path)
        c = db.cursor()
        c.execute("SELECT user_id FROM g4fusers")
        u_ids = c.fetchall()
        return u_ids
    except sqlite3.Error as e:
        print(f'get_uid ERROR! {e}')
    finally:
        if db:
            db.close()


def get_unames() -> list:
    db = None
    try:
        db = sqlite3.connect(db_path)
        c = db.cursor()
        c.execute("SELECT id, user_id, username, full_name FROM g4fusers")
        unames = c.fetchall()
        return unames
    except sqlite3.Error as e:
        print(f'get_uname ERROR! {e}')
    finally:
        if db:
            db.close()
