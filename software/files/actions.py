# This file contains Echo's actions

# Libraries
import datetime
import random
import time

import serial

arduinoData = serial.Serial(port='COM6', baudrate=9600, timeout=.1) 

def write_read(x: str): 
	arduinoData.write(bytes(x, 'utf-8')) 
	#data = arduinoData.readline() 
	#return data 


class actions():
    def time():
        return datetime.datetime.now().time().strftime('%H:%M')
    def rollDie():
        roll = random.randint(1, 6)
        write_read("1," + str(roll))
        start_time = time.time() 
        while True:
            data = arduinoData.readline().decode().strip()  
            if data:  
                return data
            elif time.time() - start_time > 5:  
                return None  # timeout occured