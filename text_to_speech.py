from gtts import gTTS
from playsound import playsound

text_response = "Jesus Christ is the central figure of Christianity, believed by Christians to be the Son of God and the savior of humanity. He is described in the New Testament as the Messiah, sent to Earth to spread the teachings of God and to save humanity from sin. Jesus is believed to have been born of a virgin, performed miracles, and ultimately died on the cross before rising from the dead. His resurrection is celebrated in the Christian holiday of Easter."
audio = gTTS(text=text_response, lang="en", slow=False)
audio.save("audio.mp3")
print("Playing audio file")
playsound("audio.mp3")