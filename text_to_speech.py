from gtts import gTTS
from playsound import playsound
import os

text_response = "stop mommy"
response = gTTS(text = text_response, lang = "en", slow = False)
response.save("response.mp3")
playsound("response.mp3")
os.remove("response.mp3")