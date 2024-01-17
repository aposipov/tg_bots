import os
import speech_recognition as sr
from pydub import AudioSegment


def ogg_to_wav(file_path):
	path_ogg = f"{file_path}.ogg"
	audio = AudioSegment.from_ogg(path_ogg)
	path_wav = f"{file_path}.wav"
	audio.export(path_wav, format='wav')
	print(path_wav)


def recognize_google(file_path_wav):
	r = sr.Recognizer()
	with sr.AudioFile(file_path_wav) as source:
		audio_data = r.record(source)
	print("recognize")
	try:
		text = r.recognize_google(audio_data, language='ru_RU')
		return text
	except sr.UnknownValueError:
		return None
	except sr.RequestError as e:
		raise ValueError(f"Ошибка при запросе к API распознавания речи: {e}")


def remove_src(path_ogg, path_wav):
	os.remove(path_ogg)
	os.remove(path_wav)
	print("delete src audio files OK")
