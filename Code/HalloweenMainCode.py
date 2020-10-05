import vlc
import time 
import serial #Import Serial Library
# from visual import * #Import all the vPython library
from vpython import *
import random

#setup
musicAvailable = True;
arduinoSerialData = serial.Serial('com3', 9600)
time.sleep(5)
readData = True


def playMusicTrack():
    musicAvailable = False;
    print("play music")
    player = vlc.MediaPlayer("D:/Unity Projects/HalloweenProject2020/Audio/Halloween-Soundtrack-v2.mp3")
    player.play()
    
    

def triggerLightSwitchON():
    print("light on")
    arduinoSerialData.write('1'.encode())

def triggerLightSwitchOFF():
    print("light off")
    arduinoSerialData.write('2'.encode())
    

def resetAll():
    musicAvailable=True
    flushSerialResp()
    time.sleep(5)
    print("----END----")


def inventionTriggered():
    playMusicTrack();
    triggerLightSwitchON();
    spinnerHandle()
    time.sleep(22)
    triggerLightSwitchOFF()
    resetAll()
    
def flushSerialResp():
    arduinoSerialData.flushInput()
    arduinoSerialData.flushOutput()

def spinnerHandle():
    random_num=random.randint(1,10)
    #start the motor for this long
    time.sleep(8)
    if (random_num%2==0):
        #open right servo
        print("TREAT")
    else:
        #open left servo
        print("TRICK")



while (readData):  #Create a loop that continues to read and display the data
    rate(50)#Tell vpython to run this loop 20 times a second
    if (arduinoSerialData.inWaiting()>0):  #Check to see if a data point is available on the serial port
        myData = arduinoSerialData.readline() #Read the distance measure as a string
        response = myData.decode('utf-8')
        if (response.rstrip()=="playSong" and musicAvailable):
            inventionTriggered();
            
