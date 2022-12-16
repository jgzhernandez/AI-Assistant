# AI-Assistant

Here is a simple AI Assistant that will answer your questions!

Once started, the program always listens and uses Voice Activity Detection (VAD) to detect when you are speaking.
Once it has heard what you asked, it uses Automatic Speech Recognition (ASR) to convert your speech to text.
This text is sent to a Large Language Model (LLM) which answers your question!
The answer to your question is then passed on to Text-to-Speech (TTS) for you to hear loud and clear.

## Implementation

In this implementation, the VAD and ASR is packaged into one using Python [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) on PyPI.
[`Recognizer.adjust_for_ambient_noise(source)`](https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#recognizer_instanceadjust_for_ambient_noisesource-audiosource-duration-float--1---none) is what handles VAD, and ASR is done using [Google Speech Recognition](https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#recognizer_instancerecognize_googleaudio_data-audiodata-key-unionstr-none--none-language-str--en-us--pfilter-union0-1-show_all-bool--false---unionstr-dictstr-any).

The LLM used is [OpenAI's cutting-edge GPT-3](https://beta.openai.com/docs/models/gpt-3) model `text-davinci-003` through OpenAI's API.

For you to hear the answer, TTS is handled by [gTTS](https://pypi.org/project/gTTS/) on PyPI.

## How to Use

**The LLM requires an OpenAI API Key.
Please visit https://beta.openai.com/account/api-keys to get one.**

To use AI-Assistant, input the following commands in your terminal:
```
git clone https://github.com/jgzhernandez/AI-Assistant
cd AI-Assistant
pip install -r requirements.txt
python assistant.py {YOUR-API-KEY}
```
Once the program is listening, you can start asking questions.
To exit the program: say "stop", "exit", or "quit".
For best results, speak to the program in an environment with minimal noise.