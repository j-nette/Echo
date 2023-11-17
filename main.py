# Run me :)

# Import functions
from software.data.files.actions import *
from software.data.files.bot import *

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
            if ai.speech_to_text() is True:
                if "goodbye Echo" in ai.text:
                    response = "Have a good one!"
                    conversation = False
                elif "time" in ai.text:
                    currentTime = actions.time()
                    response = f"It is currently {currentTime}"  
                elif "roll a die" in ai.text:
                    roll = actions.rollDie()
                    response = f"You rolled a {roll}"
                else:
                    response = str(chatBot.get_response(ai.text))
                #elif "Shutdown Echo" in ai.text:
                    #print(f" ~ Shutting down {ai.name} ~ ")
                    #run = False
            else:
                response = "I couldn't quite catch that."
            ai.text_to_speech(response)