# For bot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer as ct

# For speech
import speech_recognition as sr
from gtts import gTTS

# For data 
import os
import time
import datetime

# Chatterbot setup
echo = ChatBot(
    "Echo", 
    read_only=True,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I\'m sorry I couldn\'t quite catch that.',
            'maximum_similarity_threshold': 0.90
        }
    ])

# Training AI
trainer = ct(echo)
trainer.train("./data/corpus/")


# AI 
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
    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')


# Execute the AI
if __name__ == "__main__":
    ai = Bot(name = "Echo")
    run = True
    conversation = False

    while run is True:
        ai.speech_to_text()
        
        if "hi Echo" in ai.text:
            response = "Hello! What can I do for you today?"
            ai.text_to_speech(response)
            conversation = True
    
        while conversation is True:
            ai.speech_to_text()
            if "goodbye Echo" in ai.text:
                response = "Have a good one!"
                conversation = False
            elif "time" in ai.text:
                currentTime = ai.action_time()
                response = f"It is currently {currentTime}"
            else:
                response = echo.get_response(ai.text)
            #elif "Shutdown Echo" in ai.text:
                #print(f" ~ Shutting down {ai.name} ~ ")
                #run = False
            ai.text_to_speech(response)
