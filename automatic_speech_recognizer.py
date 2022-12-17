import torch
import speech_recognition as sr

DEVICE = torch.device('gpu' if torch.cuda.is_available() else 'cpu')


class AutomaticSpeechRecognizer:

    def __init__(self):
        self.is_on = True
        self.recognizer = sr.Recognizer()
        self.voice_recognize()

    def voice_recognize(self):
        with sr.Microphone(sample_rate=16000) as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening")
            while self.is_on:
                audio = self.recognizer.listen(source)
                try:
                    transcription = self.recognizer.recognize_google(audio)
                    print(transcription)
                except sr.UnknownValueError:
                    pass
                if transcription == "stop mommy":
                    break

