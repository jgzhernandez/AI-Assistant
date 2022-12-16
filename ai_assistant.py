import torch
import speech_recognition as sr

import openai

from gtts import gTTS
# https://realpython.com/playing-and-recording-sound-python/
import sounddevice as sd
import soundfile as sf

DEVICE = torch.device('gpu' if torch.cuda.is_available() else 'cpu')
CHATBOT_RESPONSES = []


class Assistant:
    def __init__(self):
        self.is_on = True
        self.recognizer = sr.Recognizer()
        self.voice_recognize()

    def TTS(self, text_response):
        print(text_response)
        audio = gTTS(text=text_response, lang="en", slow=False)
        audio.save("audio.wav")
        # print("Playing audio file")
        # Extract data and sampling rate from file
        data, fs = sf.read("audio.wav", dtype='float32')
        sd.play(data, fs)
        sd.wait()  # Wait until file is done playing

    def chatbot(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            temperature=0.5,
        )
        CHATBOT_RESPONSES.append(response.choices[0].text)

    def voice_recognize(self):
        with sr.Microphone(sample_rate=16000) as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            while self.is_on:
                audio = self.recognizer.listen(source)
                try:
                    transcription = self.recognizer.recognize_google(audio)
                    if len(transcription):
                        if transcription in ("stop", "exit", "quit"):
                            self.is_on = False
                            self.TTS(f"I will {transcription} now.")
                            exit()
                        self.chatbot(transcription)
                        self.TTS(CHATBOT_RESPONSES[-1].strip())
                        CHATBOT_RESPONSES.pop(-1)
                        print("Listening...")
                except sr.UnknownValueError:
                    pass
