import g4f
import asyncio

_providers = [
	# g4f.Provider.Bing, # 0203 - 200 invalid;
	g4f.Provider.GeekGpt, # 0203 - empty; 0195 ok
	# # g4f.Provider.GptChatly,
	g4f.Provider.Liaobots, # 0203 - ok; 0195 ok unauth
	g4f.Provider.Phind, # 0203 - ok; 0195 empty
	# g4f.Provider.Raycast, # 0203 - empty;
	#
	# g4f.Provider.AItianhu, # 0203 -
	# g4f.Provider.AItianhuSpace, # 0203 empty
	# g4f.Provider.AiAsk, # 0203 -
	# g4f.Provider.Aichat, # 0203 -
	g4f.Provider.ChatBase, # 0203 ok; 0195 ok
	# g4f.Provider.ChatForAi, # 0203 ok many requests
	g4f.Provider.ChatgptAi, # 0203 ok; 0195 empty
	# g4f.Provider.ChatgptX, # 0203 -
	g4f.Provider.FakeGpt, # 0203 ok; 0195 ok
	# g4f.Provider.FreeGpt, # 0203 -
	# g4f.Provider.GPTalk, # 0203 -
	# g4f.Provider.GptForLove, # 0203 -
	# g4f.Provider.GptGo, # 0203 -
	# g4f.Provider.Hashnode, # 0203 -
	# g4f.Provider.MyShell, # 0203 empty
	# g4f.Provider.NoowAi, # bad
	# g4f.Provider.OpenaiChat, # 0203 -
	# g4f.Provider.Theb, # 0203 empty
	# g4f.Provider.Vercel, # 0203 -
	# g4f.Provider.You, # 0203 -
	# g4f.Provider.Yqcloud, # 0203 -
	# g4f.Provider.Acytoo, # 0203 -
	# g4f.Provider.Aibn, # 0203 -
	# g4f.Provider.Ails, # 0195 -
	# g4f.Provider.Chatgpt4Online, # 0195 -
	# g4f.Provider.ChatgptDemo, # 0195 -
	# g4f.Provider.ChatgptDuo, # 0195
	# g4f.Provider.ChatgptFree, # 0195 -
	# g4f.Provider.ChatgptLogin, # 0195 -
	# g4f.Provider.Cromicle, # 0195 -
	# g4f.Provider.GptGod, # 0195 -
	# g4f.Provider.Opchatgpts, # 0195 -
	# g4f.Provider.Ylokh, # 0195 -
	#
	# g4f.Provider.Bard, # 0203 empty
	g4f.Provider.DeepInfra, # 0203 ok; 0195 403
	# g4f.Provider.HuggingChat, # 0203 ok kde wallet
	g4f.Provider.Llama2, # 0203 ok; 0195 ok
	# g4f.Provider.OpenAssistant, # 0203 -
]


async def run_provider(provider: g4f.Provider.BaseProvider):
	try:
		response = await g4f.ChatCompletion.create_async(
			model=g4f.models.default,
			messages=[{"role": "user", "content": "Hello"}],
			provider=provider,
		)
		print(f"{provider.__name__}:", response)
	except Exception as e:
		print(f"{provider.__name__}:", e)


async def run_all():
	calls = [
		run_provider(provider) for provider in _providers
	]
	await asyncio.gather(*calls)


asyncio.run(run_all())
