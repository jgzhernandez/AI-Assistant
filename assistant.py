import sys

import openai
from ai_assistant import Assistant

if __name__ == "__main__":
    openai.api_key = sys.argv[1]

    assistant = Assistant()
    assistant.voice_recognize()
