from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from handlers.msg_handler import set_provider, get_provider
from random import randint
import g4f

router = Router()
# PROVIDERS = ['g4f.Provider.GeekGpt', 'g4f.Provider.ChatBase', 'g4f.Provider.ChatgptAi']


def get_keyboard():
	buttons = [
		[InlineKeyboardButton(text='g4f.Provider.GeekGpt', callback_data='set_provider_1')],
		[InlineKeyboardButton(text='g4f.Provider.ChatBase', callback_data='set_provider_2')],
		[InlineKeyboardButton(text='g4f.Provider.ChatgptAi', callback_data='set_provider_3')],
		[InlineKeyboardButton(text='g4f.Provider.DeepInfra', callback_data='set_provider_4')]
		]
	keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
	return keyboard


@router.message(Command('provider'))
async def prov_handler(message: Message):
	builder = InlineKeyboardBuilder()
	# i = 0
	# for prv_name in PROVIDERS:
	await message.answer(f"Смените провайдера если бот долго не отвечает или пишет ошибку! "
	                     f"Текущий провайдер -> \n {get_provider()}")
	# builder.add(InlineKeyboardButton(text='g4f.Provider.GeekGpt',
	#                                  callback_data='set_provider_1'))
	# builder.add(InlineKeyboardButton(text='g4f.Provider.ChatBase',
	#                                  callback_data='set_provider_2'))
	# builder.add(InlineKeyboardButton(text='g4f.Provider.ChatgptAi',
	#                                  callback_data='set_provider_3'))
	await message.answer(
		'Нажмите на кнопку чтобы сменить провайдера!',
		reply_markup=get_keyboard()
	)


@router.message(Command("random"))
async def cmd_random(message: Message):
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(
		text="Нажми меня",
		callback_data="random_value")
	)
	await message.answer(
		"Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
		reply_markup=builder.as_markup()
	)


@router.callback_query(F.data == "random_value")
async def send_random_value(callback: CallbackQuery):
	await callback.message.answer(str(randint(1, 10)))


@router.callback_query(F.data == "set_provider_1")
async def send_random_value(callback: CallbackQuery):
	provider = g4f.Provider.GeekGpt
	set_provider(provider)
	await callback.message.answer(f'✅ {provider} провайдер установлен')


@router.callback_query(F.data == "set_provider_2")
async def send_random_value(callback: CallbackQuery):
	provider = g4f.Provider.ChatBase
	set_provider(provider)
	await callback.message.answer(f'✅ {provider} провайдер установлен')


@router.callback_query(F.data == "set_provider_3")
async def send_random_value(callback: CallbackQuery):
	provider = g4f.Provider.ChatgptAi
	set_provider(provider)
	await callback.message.answer(f'✅ {provider} провайдер установлен!')


@router.callback_query(F.data == "set_provider_4")
async def send_random_value(callback: CallbackQuery):
	provider = g4f.Provider.DeepInfra
	set_provider(provider)
	await callback.message.answer(f'✅ {provider} провайдер установлен!')
