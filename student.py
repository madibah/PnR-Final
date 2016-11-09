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
    class Pigo(object):
        MIDPOINT = 97
        STOP_DIST = 20
        RIGHT_SPEED = 200
        speed = 100
        LEFT_SPEED = 150
        scan = [None] * 180

    # CONSTRUCTOR
    def __init__(self):
        print("Piggy has be instantiated!")
        # this method makes sure Piggy is looking forward
        #self.calibrate()
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)
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

    def isClear(self) -> bool:
        for x in range((self.MIDPOINT - 15), (self.MIDPOINT + 15), 5):
            servo(x)
            time.sleep(.1)
            scan1 = us_dist(15)
            time.sleep(.1)
            # double check the distance
            scan2 = us_dist(15)
            time.sleep(.1)
            # if I found a different distance the second time....
            if abs(scan1 - scan2) > 2:
                scan3 = us_dist(15)
                time.sleep(.1)
                # take another scan and average the three together
                scan1 = (scan1 + scan2 + scan3) / 3
            self.scan[x] = scan1
            print("Degree: " + str(x) + ", distance: " + str(scan1))
            if scan1 < self.STOP_DIST:
                print("Doesn't look clear to me")
                return False
        return True

    def cruise(self):
        set_left_speed (115)
        set_right_speed (115)
        print("Is it clear in front of me?")
        clear = self.isClear()
        print(clear)
        while True:
            if clear:
                print("Let's roll...")
                fwd()
            if not self.isClear():
                print("OMG STOP!!!!")
                self.stop()
                answer = self.choosePath()
                if answer == "left":
                    self.encL(4)
                elif answer == "right":
                    self.encR(4)

    def setSpeed(self, left, right):
        set_left_speed(left)
        set_right_speed(right)
        self.LEFT_SPEED = left
        self.RIGHT_SPEED = right
        print('Left speed set to: ' + str(left) + ' // Right set to: ' + str(right))

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



            ###print(" Choice " + str(count) + " is at " + str(x) + " degrees. ")

            def dataBase(self):
                menu = {"1": (" Direction Left Four", self.leftTurn4),
                        "2": (" Direction Left Two", self.leftTurn2),
                        "3": (" Direction Forward Four", self.forward4),
                        "4": (" Direction Forward Eight", self.forward8),
                        "5": (" Direction Right Two", self.rightTurn2),
                        "6": (" Direction Right Four", self.rightTurn4),
                        "n": (" Return to testDrive", self.testDrive),
                        "q": (" Return to selection menu", self.handler)
                        }
                # loop and print the menu...
                for key in sorted(menu.keys()):
                    print(key + ":" + menu[key][0])
                #
                ans = input("Your selection: ")
                menu.get(ans, [None, error])[1]()

                # ans = input("Your selection: ")
                # option.get(ans, [None, error])[1]()

            def rightTurn4(self):
                self.encR(4)

            def rightTurn2(self):
                self.encR(2)

            def leftTurn4(self):
                self.encL(4)

            def leftTurn2(self):
                self.encL(2)

            def forward4(self):
                self.encF(4)

            def forward8(self):
                self.encF(8)
                # TODO figure out what option is closest to the midpoint

                ##########################################################
                ####### Calibration methods and turn speed help

            def setSpeed(self, x):
                self.speed = x
                set_left_speed(self.speed * .3)
                set_right_speed(speed)

            def getSpeed(self):
                return self.speed

                ########################################################
                ########## Consistent turns

            def turnR(self, x):
                previous = self.getSpeed()
                self.setSpeed(self.TURNSPEED)
                self.encR(x)
                self.setSpeed(previous)

            def turnL(self, x):
                previous = self.getSpeed()
                self.setSpeed(self.TURNSPEED)
                self.encL(x)
                self.setSpeed(previous)

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
