
# This file contains basic Echo interactions. This includes TTS, responses, and STT.


# For bot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer as ct

import time

# For speech
import speech_recognition as sr
from gtts import gTTS
import os

# For Audio File
from mutagen.mp3 import MP3

def get_length():
    audio = MP3("./data/files/response.mp3")
    length = audio.info.length + 2 # extra 2 seconds for loading the file
    #print(length)
    return length

# Chatterbot setup
chatBot = ChatBot(
    "Echo", 
    read_only=True,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I\'m sorry I don\'t quite understand.',
            'maximum_similarity_threshold': 0.90
        }
    ])

# Training Echo
trainer = ct(chatBot)
trainer.train("./data/corpus/")

class Bot():
    def __init__(self, name):
        print(" ~ Starting up", name,"~ ")
        self.name = name
        self.text = ""

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("Me :", self.text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition; {0}".format(e)) 

    def text_to_speech(self, text: str):
        print(self.name, ": ", text)
        speaker = gTTS(text = text, lang = "en", slow = False)
        # Store, open, and cleanup temporary audio file
        speaker.save("./data/files/response.mp3") 
        os.system("start ./data/files/response.mp3")  
        time.sleep(get_length()) # delay to avoid cleaning the file up before it is done playing
        os.remove("./data/files/response.mp3")