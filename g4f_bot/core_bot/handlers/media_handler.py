from aiogram import Router, F
from aiogram.types import Message
from utils.voice_u import ogg_to_wav, recognize_google, remove_src

router = Router()


@router.message(F.photo)
async def photo_handler(message: Message):
	await message.answer("⚠️ Фотографии пока не обрабатываются. "
	                     "Функция в разработке 😉")


@router.message(F.voice)
async def voice_handler(message: Message):
	from main import bot
	file_id = message.voice.file_id
	file = await bot.get_file(file_id)
	file_path = file.file_path
	print(file_path)
	file_path_ogg = f"{file_path}.ogg"
	file_path_wav = f"{file_path}.wav"
	print(file_path_ogg)
	await bot.download_file(file_path, file_path_ogg)
	answer_msg = await message.answer("распознавание голосового сообщения 🧐")
	await ogg_to_wav(file_path)
	text = await recognize_google(file_path_wav)
	await answer_msg.delete()
	if text:
		await message.answer(text)
	else:
		await message.answer("⚠️ Не удалось распознать речь!")
	print('text OK')
	await remove_src(file_path_ogg, file_path_wav)


@router.message(F.content_type.in_({'voice', 'video', 'audio'}))
async def media_handler(message: Message):
	await message.answer("⚠️ Медиафайлы пока не обрабатываются. "
		                     "Функция в разработке 😉")
