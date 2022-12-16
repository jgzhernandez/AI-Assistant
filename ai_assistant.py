import torch
import speech_recognition as sr
import openai

openai.api_key = "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"
DEVICE = torch.device('gpu' if torch.cuda.is_available() else 'cpu')
CHATBOT_RESPONSES = []


class Assistant:

    def __init__(self):
        self.is_on = True
        self.recognizer = sr.Recognizer()
        self.voice_recognize()

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
            print("Listening")
            while self.is_on:
                audio = self.recognizer.listen(source)
                try:
                    transcription = self.recognizer.recognize_google(audio)
                    if transcription:
                        self.chatbot(transcription)
                        print(CHATBOT_RESPONSES[-1])
                        CHATBOT_RESPONSES.pop(-1)
                except sr.UnknownValueError:
                    pass

