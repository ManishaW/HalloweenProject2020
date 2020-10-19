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
    

def pullUpLever():
    print("light on")
    arduinoSerialData.write('1'.encode())

def pullDownLever():
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
    pullUpLever();
    spinnerHandle()
    await p.turn_on()
    treatDispense()
    time.sleep(20)

    pullDownLever()
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
    arduinoSerialData.write('4'.encode())
    time.sleep(9);    
    
    

def treatDispense():
    time.sleep(1)
    if (random_num%2==0):
        print("TREAT")
        releaseTricks();
    else:
        # #open left servo
        #   #open right servo
        # time.sleep(4);
        # # arduinoSerialData.write('3'.encode())
        # print("TREAT")
        # time.sleep(8)
        # # releaseTreats();
        # arduinoSerialData.write('4'.encode())
        print("TREAT")
        releaseTricks();


#main
playerBkgd = vlc.MediaPlayer("D:/Unity Projects/HalloweenProject2020/Audio/Ambience3.mp3")
# while (True):


while (readData):  #Create a loop that continues to read and display the data
    rate(50)#Tell vpython to run this loop 20 times a second
    if (True): playerBkgd.play()
    if (arduinoSerialData.inWaiting()>0):  #Check to see if a data point is available on the serial port
        myData = arduinoSerialData.readline() #Read the distance measure as a string
        response = myData.decode('utf-8')
        if (response.rstrip()=="playSong" and musicAvailable):
            asyncio.run(inventionTriggered());
            

