
# This file contains basic Echo interactions. This includes TTS, responses, and STT.


# For bot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer as ct

# For speech
import speech_recognition as sr
from gtts import gTTS

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

    def text_to_speech(self, text):
        print(self.name, ": ", text)
        #speaker = gTTS(text = text, lang = "en", slow = False)
        # Store, open, and cleanup temporary audio file
        #speaker.save("response.mp3") 
        #os.system('start response.mp3')  
        #os.remove("response.mp3")