from db.requests import get_uids


async def shout(text: str):
	from main import bot
	print("SHOUT!")
	u_ids = get_uids()
	for u in u_ids:
		print(u[0])
		try:
			await bot.send_message(chat_id=u[0], text=text)
		except Exception as e:
			print(f'shout ERROR! {e}')
