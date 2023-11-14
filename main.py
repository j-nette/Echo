# For bot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer as ct

# Import functions
from data.files.actions import *
from data.files.bot import *

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
                currentTime = actions.time()
                response = f"It is currently {currentTime}"
            else:
                response = chatBot.get_response(ai.text)
            #elif "Shutdown Echo" in ai.text:
                #print(f" ~ Shutting down {ai.name} ~ ")
                #run = False
            ai.text_to_speech(response)