import vlc
import time 
import serial #Import Serial Library
# from visual import * #Import all the vPython library
from vpython import *


def playMusicTrack():
    print("play music")
    player = vlc.MediaPlayer("D:/Unity Projects/HalloweenProject2020/Audio/Halloween-Soundtrack-v2.mp3")
    player.play()
    # time.sleep(30)

arduinoSerialData = serial.Serial('com3', 9600)
while (1==1):  #Create a loop that continues to read and display the data
    rate(50)#Tell vpython to run this loop 20 times a second
    if (arduinoSerialData.inWaiting()>0):  #Check to see if a data point is available on the serial port
        myData = arduinoSerialData.readline() #Read the distance measure as a string
        response = myData.decode('utf-8')
        if (response.rstrip()=="playSong"):
            playMusicTrack();


