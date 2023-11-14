# This file contains Echo's actions

# Libraries
import datetime

class actions():
    def time():
        return datetime.datetime.now().time().strftime('%H:%M')

    