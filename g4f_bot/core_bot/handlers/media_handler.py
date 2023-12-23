from aiogram import Router, F
from aiogram.types import Message, ContentType

router = Router()


@router.message(F.photo)
async def photo_handler(message: Message):
	await message.answer("Фотографии пока не обрабатываются. "
	                     "Функция в разработке 😉")


@router.message(F.content_type.in_({'voice', 'video', 'audio'}))
async def media_handler(message: Message):
	# if message.voice:
		await message.answer("Медиафайлы пока не обрабатываются. "
		                     "Функция в разработке 😉")
