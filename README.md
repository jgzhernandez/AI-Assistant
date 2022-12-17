# AI-Assistant
Mombot is an AI Voice Assistant with four different stages of operation: Voice Activity Detection, Automatic Speech Recognition, Large Language Model, and Text to Speech. 

The Voice Activiy Detection (VAD) model is implemented using Silero VAD. It is a pre-trained VAD model uploaded in GitHub through the link https://github.com/snakers4/silero-vad. It detects voice to activate the Automatic Speech Recognizer (ASR). The wake word for Mombot is "Hello Mommy".

The ASR Module is implemented using the Speech Recognition API which is imported as speech_recognition. This listens to the user and transcribes what was said before sending it to the Chatbot. 

The Chatbot needs an API key, since the API is not that open or accessible. If the credits of the key has expired, a new key needs to be used. 

When an answer has been provided, Google's Text-to-Speech module is used for Mombot to say the answer out loud. Mombot can be deactivated when you say "Goodbye Mommy!"