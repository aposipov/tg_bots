import g4f

conversation_history = {}
PROVIDERSET = g4f.Provider.GeekGpt


def set_provider(provider):
	global PROVIDERSET
	PROVIDERSET = provider
	print(PROVIDERSET)


# def get_provider():
# 	print(PROVIDERSET)
# 	return PROVIDERSET


def trim_history(history, max_length=4096):
	current_length = sum(len(message["content"]) for message in history)
	while history and current_length > max_length:
		removed_message = history.pop(0)
		current_length -= len(removed_message["content"])
	return history


async def gpt_processing(user_input, user_id):
	# global conversation_history
	prv_name = PROVIDERSET
	print(user_input)
	if user_id not in conversation_history:
		conversation_history[user_id] = []
	conversation_history[user_id].append({"role": "user", "content": user_input})
	conversation_history[user_id] = trim_history(conversation_history[user_id])
	chat_history = conversation_history[user_id]
	try:
		response = await g4f.ChatCompletion.create_async(
			model=g4f.models.default,
			messages=chat_history,
			provider=prv_name,
		)
		chat_gpt_response = response
	except Exception as e:
		print(f"gpt_processing error {e}")
		chat_gpt_response = "⚠️ Упс, что-то пошло не так. " \
							"Попробуйте еще раз! Или напишите запрос иначе! " \
							"Возможно ошибки на стороне провайдера и нужно подождать! " \
							"Или сменить провайдера /provider"
	conversation_history[user_id].append({"role": "assistant", "content": chat_gpt_response})
	length = sum(len(message["content"]) for message in conversation_history[user_id])
	print(length)
	print(chat_gpt_response)
	return chat_gpt_response
