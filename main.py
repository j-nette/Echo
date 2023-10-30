# For bot, not used currently
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer as ct

# For speech
import speech_recognition as sr
from gtts import gTTS

# For data 
import os

class Bot():
    def __init__(self, name):
        print(" ~ Starting up", name,"~ ")
        self.name = name

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("Me:", self.text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition; {0}".format(e)) 

    def text_to_speech(self, text):
        print(self.name, ":", text)
        speaker = gTTS(text = text, lang = "en", slow = False)
        # Store, open, and cleanup temporary audio file
        speaker.save("res.mp3") 
        os.system('start res.mp3')  
        os.remove("res.mp3")

    def wake_up(self, text):
        return True if self.name in text.lower() else False
    

# Execute the AI
if __name__ == "__main__":
    ai = Bot(name = "Echo")
    run = True
    conversation = False
    res = ""

    while run is True:
        ai.speech_to_text()
        
        if "Hi Echo" in ai.text:
            res = "Hello! What can I do for you today?"
            conversation = True
        elif "Shutdown Echo" in ai.text:
            print(f" ~ Closing down {ai.name} ~ ")

        while conversation is True:
            if "Bye Echo" in ai.text:
                res = "Have a good one"
                conversation = False
            else:
                res = "Sorry, I couldn't quite get that. Come again?"
        print("Echo: ", res)
        ai.text_to_speech(res)
