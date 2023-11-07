# Echo
Desktop assistant that responds to speech commands.

## Features
1. To wake Echo up, say "Hi Echo"
2. To put Echo back to sleep, say "Goodbye Echo"
3. To check the current time, ask Echo "what time is it?

# Requirements
```
pip install python-dotenv

pip install speechrecognition
pip install gTTS
pip install chatterbot==1.0.4
pip install pytz

pip install googlesearch-python

pip install -e git+https://github.com/yeahwhat-mc/goslate#egg=goslate
pip install PyDictionary
```

## Errors with Libraries 
1. AttributeError: module 'time' has no attribute 'clock'
    - Solution: time.clock is reprecated. You can click on the path to the error and modify time.clock to time.time or downgrade to Python 3.7.
2. AttributeError: module 'yaml' has no attribute 'safe'
    - Solution: Click on the path to the error and modify yaml.load() to yaml.safe_load().
3. You need to install goslate before installing PyDictionary. 