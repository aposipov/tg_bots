import asyncio
import sqlite3
import aiosqlite
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


def add_data(message: Message):
    user_id: int = message.from_user.id
    username: str = '@' + message.from_user.username
    full_name: str = message.from_user.full_name
    lang: str = message.from_user.language_code
    date = message.date
    try:
        db = sqlite3.connect('data/dev_g4f.db')
        c = db.cursor()
        c.execute("INSERT INTO g4fusers VALUES (?,?,?,?,?)",
                  (user_id, username, full_name, lang, date))
        db.commit()
        db.close()
        print(f'User {user_id} added to DB!')
    except sqlite3.Error as e:
        print(f'add_data ERROR! {e}')


def get_uid() -> list:
    try:
        db = sqlite3.connect('data/dev_g4f.db')
        c = db.cursor()
        c.execute("SELECT user_id FROM g4fusers")
        u_ids = c.fetchall()
        return u_ids
    except sqlite3.Error as e:
        print(f'get_uid ERROR! {e}')


def get_uname() -> list:
    try:
        db = sqlite3.connect('data/dev_g4f.db')
        c = db.cursor()
        c.execute("SELECT username FROM g4fusers")
        unames = c.fetchall()
        return unames
    except sqlite3.Error as e:
        print(f'get_uname ERROR! {e}')
