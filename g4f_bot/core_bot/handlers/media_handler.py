import os
import asyncio
from aiogram import Router, F
from aiogram.types import Message
import speech_recognition as sr
from pydub import AudioSegment

router = Router()


async def recognize_google(file_path_wav):
	recognizer = sr.Recognizer()
	with sr.AudioFile(file_path_wav) as source:
		audio_data = recognizer.record(source)
	print("process")
	try:
		text = recognizer.recognize_google(audio_data, language='ru-RU')
		return text
	except sr.UnknownValueError:
		return None
	except sr.RequestError as e:
		raise ValueError(f"Ошибка при запросе к API распознавания речи: {e}")


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
	print(file_path_ogg)
	await bot.download_file(file_path, file_path_ogg)
	answer_msg = await message.answer("распознавание голосового сообщения 🧐")

	#convert await
	audio = AudioSegment.from_ogg(file_path_ogg)
	file_path_wav = f"{file_path}.wav"
	audio.export(file_path_wav, format="wav")
	print(file_path_wav)

	#recognize await
	# try:
	text = await recognize_google(file_path_wav)
	await answer_msg.delete()
	if text:
		await message.answer(text)
	else:
		await message.answer("⚠️ Не удалось распознать речь!")
	print('ok')

	# except sr.UnknownValueError:
	# 	await message.answer("⚠️ Не удалось распознать речь. EXCEPT")
	# except sr.RequestError as e:
	# 	await message.answer(
	# 		f"⚠️ Ошибка при запросе к API распознавания речи EXCEPT: {e}")
	# finally:
		# Удаление временного файла
	os.remove(file_path_ogg)
	os.remove(file_path_wav)


@router.message(F.content_type.in_({'voice', 'video', 'audio'}))
async def media_handler(message: Message):
	await message.answer("⚠️ Медиафайлы пока не обрабатываются. "
		                     "Функция в разработке 😉")
