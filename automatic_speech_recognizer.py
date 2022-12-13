import torch
from pydub import AudioSegment
from io import BytesIO
import speech_recognition as sr

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
MODEL, DECODER, UTILS = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                       model='silero_stt', language='en', device=DEVICE)


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
                audio = BytesIO(audio.get_wav_data())
                audio = AudioSegment.from_file(audio, format="wav")
                input_tensor = torch.FloatTensor(audio.get_array_of_samples()).view(1, -1)
                input_tensor = input_tensor.to(DEVICE)
                output_tensor = MODEL(input_tensor)
                transcription = DECODER(output_tensor[0])
                print(transcription)
