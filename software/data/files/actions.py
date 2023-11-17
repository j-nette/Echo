# This file contains Echo's actions

# Libraries
import datetime
import random
import time

import serial

arduinoData = serial.Serial(port='COM6', baudrate=9600, timeout=.1) 

def write_read(x: str): 
	arduinoData.write(bytes(x, 'utf-8')) 
	time.sleep(0.05) 
	data = arduinoData.readline() 
	return data 

class actions():
    def time():
        return datetime.datetime.now().time().strftime('%H:%M')
    def rollDie():
        while True:
            roll = random.randint(1, 6)
            done = write_read("1," + str(roll))
            if done:
                return roll
            else: # waiting for the code on the Arduino side to finish
                time.sleep(0.1)
    