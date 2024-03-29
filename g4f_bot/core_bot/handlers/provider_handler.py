from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
# from handlers.msg_handler import set_provider, get_provider
from utils.provider_u import set_provider
from random import randint
import g4f

router = Router()
# g4f.Provider.GeekGpt g4f.Provider.ChatBase g4f.Provider.ChatgptAi
# g4f.Provider.FakeGpt g4f.Provider.Llama2 g4f.Provider.DeepInfra
cur_prov = 'set_provider_1'


def set_prov(prov: str):
	global cur_prov
	cur_prov = prov


def get_keyboard():
	global cur_prov
	buttons = [
		[InlineKeyboardButton(text='Provider -> GeekGpt', callback_data='set_provider_1')],
		[InlineKeyboardButton(text='Provider -> ChatBase', callback_data='set_provider_2')],
		[InlineKeyboardButton(text='Provider -> ChatgptAi', callback_data='set_provider_3')],
		[InlineKeyboardButton(text='Provider -> FakeGpt', callback_data='set_provider_4')],
		[InlineKeyboardButton(text='Provider -> DeepInfra', callback_data='set_provider_5')],
		[InlineKeyboardButton(text='Provider -> Llama2', callback_data='set_provider_6')]
		]
	if cur_prov:
		for row in buttons:
			for btn in row:
				if btn.callback_data == cur_prov:
					btn.text = btn.text + ' ✔️'

	keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
	return keyboard


@router.message(Command('provider'))
async def prov_handler(message: Message):
	await message.answer(f"Смените провайдера если бот долго не отвечает или пишет ошибку! ")
	await message.answer(
		'Выберите провайдера!',
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
async def prov_init_1(callback: CallbackQuery):
	provider = g4f.Provider.GeekGpt
	set_prov("set_provider_1")
	set_provider(provider)
	await callback.message.answer(text="Провайдер изменен!",
	                              reply_markup=get_keyboard())


@router.callback_query(F.data == "set_provider_2")
async def prov_init_2(callback: CallbackQuery):
	provider = g4f.Provider.ChatBase
	set_prov("set_provider_2")
	set_provider(provider)
	await callback.message.answer(text="Провайдер изменен!", reply_markup=get_keyboard())
	# await callback.answer(text=f"{provider}", show_alert=True)


@router.callback_query(F.data == "set_provider_3")
async def prov_init_3(callback: CallbackQuery):
	provider = g4f.Provider.ChatgptAi
	set_prov("set_provider_3")
	set_provider(provider)
	await callback.message.answer(text="Провайдер изменен!",
	                              reply_markup=get_keyboard())


@router.callback_query(F.data == "set_provider_4")
async def prov_init_4(callback: CallbackQuery):
	provider = g4f.Provider.FakeGpt
	set_prov("set_provider_4")
	set_provider(provider)
	await callback.message.answer(text="Провайдер изменен!",
	                              reply_markup=get_keyboard())


@router.callback_query(F.data == "set_provider_5")
async def prov_init_4(callback: CallbackQuery):
	provider = g4f.Provider.DeepInfra
	set_prov("set_provider_5")
	set_provider(provider)
	await callback.message.answer(text="Провайдер изменен!",
	                              reply_markup=get_keyboard())


@router.callback_query(F.data == "set_provider_6")
async def prov_init_4(callback: CallbackQuery):
	provider = g4f.Provider.Llama2
	set_prov("set_provider_6")
	set_provider(provider)
	await callback.message.answer(text="Провайдер изменен!",
	                              reply_markup=get_keyboard())