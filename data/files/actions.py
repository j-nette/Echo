# This file contains Echo's actions

# Libraries
import datetime

#from googlesearch import search
#from bs4 import BeautifulSoup
#import requests

from PyDictionary import PyDictionary 
dictionary=PyDictionary()

import os
from dotenv import load_dotenv

load_dotenv()
weather_api_key = os.getenv('WEATHER_API_KEY')

class actions():
    def time():
        return datetime.datetime.now().time().strftime('%H:%M')
    
    def define(query):
        return dictionary.meaning(query)
    