import vlc
import time 
import serial #Import Serial Library
# from visual import * #Import all the vPython library
from vpython import *
import random
import asyncio
from kasa import SmartPlug
from kasa import Discover


devices = asyncio.run(Discover.discover())
p = SmartPlug("192.168.1.29")

#setup
musicAvailable = True;
arduinoSerialData = serial.Serial('com3', 9600)
time.sleep(5)
readData = True
random_num =-1

def playMusicTrack():
    musicAvailable = False;
    print("play music")
    player = vlc.MediaPlayer("D:/Unity Projects/HalloweenProject2020/Audio/Halloween-Soundtrack-v3.mp3")
    player.play()
    

def triggerLightSwitchON():
    print("light on")
    arduinoSerialData.write('1'.encode())

def triggerLightSwitchOFF():
    print("light off")
    arduinoSerialData.write('2'.encode())


def resetAll():
    
    
    if (random_num%2==0):
        #DO SOMETHING
        arduinoSerialData.write('5'.encode())
        time.sleep(5)
    
    else:
        #Do something
        arduinoSerialData.write('6'.encode())
    arduinoSerialData.write('r'.encode())
    time.sleep(3)
    flushSerialResp()
    musicAvailable=True
    print("----END----")


async def inventionTriggered():
    playerBkgd.stop()
    playMusicTrack();
    triggerLightSwitchON();
    await p.turn_on()
    spinnerHandle()
    time.sleep(19)
    triggerLightSwitchOFF()
    await p.turn_off()
    resetAll()
    playerBkgd.play()
    
def flushSerialResp():
    arduinoSerialData.flushInput()
    arduinoSerialData.flushOutput()

def releaseTreats():
    arduinoSerialData.write('8'.encode())
def releaseTricks():
    arduinoSerialData.write('7'.encode())


def spinnerHandle():
    
    random_num=random.randint(0,5)
    print(random_num)
    #start the motor for this long
   
    if (random_num%2==0):
        #open right servo
        time.sleep(2);
        arduinoSerialData.write('3'.encode())
        print("TREAT")
        time.sleep(8)
        releaseTreats();
    else:
        #open left servo
        time.sleep(2);
        arduinoSerialData.write('4'.encode())
        print("TRICK")
        time.sleep(8)
        releaseTricks();



#main
playerBkgd = vlc.MediaPlayer("D:/Unity Projects/HalloweenProject2020/Audio/Ambience.mp3")
playerBkgd.play()

while (readData):  #Create a loop that continues to read and display the data
    rate(50)#Tell vpython to run this loop 20 times a second
    if (arduinoSerialData.inWaiting()>0):  #Check to see if a data point is available on the serial port
        myData = arduinoSerialData.readline() #Read the distance measure as a string
        response = myData.decode('utf-8')
        if (response.rstrip()=="playSong" and musicAvailable):
            asyncio.run(inventionTriggered());
            

