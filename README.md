# AI-Assistant

Remember when you used to ask your mom things and she would answer your every burning question? Relive that experience with Mombot!

Mombot is an AI Voice Assistant with four different stages of operation: Voice Activity Detection (VAD), Automatic Speech Recognition (ASR), Large Language Model (LLM), and Text-to-Speech (TTS).

## Implementation

Once started, Mombot always listens using VAD to know when you are talking specifically to Mombot.

In this implementation, the VAD and ASR is packaged into one using Python [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) on PyPI.
[`Recognizer.adjust_for_ambient_noise(source)`](https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#recognizer_instanceadjust_for_ambient_noisesource-audiosource-duration-float--1---none) is what handles VAD, and ASR is done using [Google Speech Recognition](https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#recognizer_instancerecognize_googleaudio_data-audiodata-key-unionstr-none--none-language-str--en-us--pfilter-union0-1-show_all-bool--false---unionstr-dictstr-any).

The LLM used is [OpenAI's cutting-edge GPT-3](https://beta.openai.com/docs/models/gpt-3) model `text-davinci-003` through OpenAI's API.
The Chatbot needs an API key from OpenAI, since the API is not that open or accessible.
If the credits of the key has expired or is detected to be made public, a new key needs to be used. 

When an answer has been provided, [Google's Text-to-Speech module](https://pypi.org/project/gTTS/) is used for Mombot to say the answer out loud.

## How to Use

**The LLM requires an OpenAI API Key.
Please visit https://beta.openai.com/account/api-keys to get one.**

To use Mombot, input the following commands in your terminal:
```
git clone https://github.com/jgzhernandez/AI-Assistant
cd AI-Assistant
pip3 install -r requirements.txt
python3 assistant.py
```
Mombot will then pop up and wait for you to say "Hello Mommy".
Mombot will also let you know when you are being listened to.
During this time, you can ask your question.
Mombot will stop listening and remain idle when you say the phrase "Thank you, Mom!" 
Mombot can be deactivated when you say "Goodbye Mom!"
