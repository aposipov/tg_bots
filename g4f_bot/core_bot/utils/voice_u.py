import os
import speech_recognition as sr
import subprocess
import json
from vosk import KaldiRecognizer, Model, SetLogLevel
from pydub import AudioSegment

MODEL_PATH = 'data/vosk-small'


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
	print("Recognizing...")
	try:
		text = r.recognize_google(audio_data, language='ru_RU')
		return text
	except sr.UnknownValueError:
		return None
	except sr.RequestError as e:
		raise ValueError(f"Ошибка при запросе к API распознавания речи: {e}")


def recognize_vosk(file_path_wav):
	sample_rate = 16000
	SetLogLevel(0)
	model = Model(MODEL_PATH)
	rec = KaldiRecognizer(model, sample_rate)
	with subprocess.Popen(["ffmpeg", "-loglevel", "quiet", "-i",
							file_path_wav,
							"-ar", str(sample_rate), "-ac", "1", "-f", "s16le",
							"-"],
							stdout=subprocess.PIPE) as process:
		while True:
			data = process.stdout.read(4000)
			if len(data) == 0:
				break
			if rec.AcceptWaveform(data):
				rec.Result()
			else:
				rec.PartialResult()
	text = json.loads(rec.FinalResult())
	return text['text']


def remove_src(path_ogg, path_wav):
	os.remove(path_ogg)
	os.remove(path_wav)
	print("delete src audio files OK")
