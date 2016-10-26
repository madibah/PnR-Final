import pigo
import time
import random
from gopigo import *

'''
This class INHERITS your teacher's Pigo class. That means Mr. A can continue to
improve the parent class and it won't overwrite your work.
'''


class GoPiggy(pigo.Pigo):
    # CUSTOM INSTANCE VARIABLES GO HERE. You get the empty self.scan array from Pigo
    # You may want to add a variable to store your default speed
    MIDPOINT = 97
    STOP_DIST = 20

    # CONSTRUCTOR
    def __init__(self):
        print("Piggy has be instantiated!")
        # this method makes sure Piggy is looking forward
        #self.calibrate()
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.handler()

    ##### HANDLE IT
    def handler(self):
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like
        menu = {"1": ("Navigate forward", self.nav),
                "2": ("Rotate", self.rotate),
                "3": ("Dance", self.dance),
                "4": ("Calibrate servo", self.calibrate),
                "5": ("Cruise", self.cruise),
                "q": ("Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        #
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

    def cruise(self):
        print("Is it clear in front of me?")
        clear = self.isClear()
        print(clear)
        if clear:
            print("Let's roll...")
            fwd()
        while True:
            if not self.isClear():
                print("OMG STOP!!!!")
                self.stop()

    # A SIMPLE DANCE ALGORITHM
    def dance(self):
        print("Piggy dance")
        ##### WRITE YOUR FIRST PROJECT HERE
        print ('is it safe to dance')
        x = 100
        while self.isClear() and x <= 200:
            self.encR(18)
            print ('speed is set to:' + str(x))
            set_speed(x)
            servo(20)
            self.encB(10)
            self.encR(20)
            self.encL(10)
            self.encB(20)
            self.encF(10)
            servo(130)
            self.encL(20)
            self.encF(20)
            self.encB(8)
            self.encL(10)
            self.encL(10)
            self.encR(10)
            self.encR(10)
            self.encB(8)
            self.encF(8)
            servo(80)
            self.encF(8)
            self.encL(10)
            self.encB(10)
            self.encL(8)
            self.encB(10)
            self.encL(8)
            servo(120)
            time.sleep(.4)
            x += 25



    # AUTONOMOUS DRIVING
    def nav(self):
        print("Piggy nav")
        ##### WRITE YOUR FINAL PROJECT HERE
        #TODO: If while loop fails, check for other paths
        #loop: check that it's clear
        while True:
            while self.isClear():
                #let's go forward just a little bit
                self.encF(5)
            answer = self.choosePath()
            if answer == "left":
                self.encL(3)
            elif answer == "right":
                self.encR(3)




####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
