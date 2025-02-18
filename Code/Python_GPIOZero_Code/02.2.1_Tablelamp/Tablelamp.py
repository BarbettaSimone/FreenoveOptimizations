#!/usr/bin/env python3
########################################################################
# Filename    : Tablelamp.py
# Description : DIY MINI table lamp
# Author      : www.freenove.com
# modification: 2023/05/11
########################################################################
from gpiozero import LED, Button
import time
from threading import Lock

led = LED(17) # define LED pin according to BCM Numbering
button = Button(18) # define Button pin according to BCM Numbering
currentTime = time.time()

def onButtonPressed():  # When button is pressed, this function will be executed
    global currentTime
    """
    To avoid double onButtonPressed()
    caused by the button
    """
    if (time.time() - currentTime > 0.5):
        led.toggle()
        if led.is_lit :
            print("Led turned on >>>")
        else :
            print("Led turned off <<<")
        currentTime = time.time()
        
def loop():
    #Button detect
    button.when_pressed = onButtonPressed
    while True:
        time.sleep(1)
def destroy():
    led.close()
    button.close()    
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        print("Ending program")