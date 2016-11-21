import pigo
import time
import random
from gopigo import *

'''
This class INHERITS your teacher's Pigo class. That means Mr. A can continue to
improve the parent class and it won't overwrite your work.
'''
LEFT_SPEED = 100
RIGHT_SPEED = 100

class GoPiggy(pigo.Pigo):
    # CUSTOM INSTANCE VARIABLES GO HERE. You get the empty self.scan array from Pigo
    # You may want to add a variable to store your default speed
    class Pigo(object):
        MIDPOINT = 97
        STOP_DIST = 20
        speed = 100
        scan = [None] * 180
        LEFT_SPEED = 200
        RIGHT_SPEED = 200


        turn_track = 0.00
        TIME_PER_EGREE = 0.011
        TURN_MODIFIER = .5


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
                "5": ("Cruise", self.cruise)

                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        #
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

######## Big self driving method
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

    #### New turn methods because encR and encl just don't cut it
    ### take number of degrees and turns right accordingly
    def turnR(self, deg):
         #blah blah blah
        self.turn_track += deg
        print("let's turn"+ str(self.turn_trak) + " degrees away")
        right_rot()
        time.sleep(self.TIME_PER_DEGREE)
        self.stop()

    def turnL(self, deg):
        # blah blah blah
        self.turn_track += deg
        print("let's turn" + str(self.turn_trak) + " degrees away")
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER, self.RIGHT_SPEED * self.TURN_MODIFIER)
        #do turn stuff
        left_rot()
        time.sleep(deg * self.TIME_PER_DEGREE)
        self.stop()
        self.setspeed(self.LEFT_SPEED, self.RIGHT_SPEED)



    def setSpeed(self, left, right):
        print("left speed: " + str(left)) + '// "right speed: " '+ str(right))
        set_left_speed(int(left))
        set_right_speed(int(right))
        self.LEFT_SPEED = left
        self.RIGHT_SPEED = right
        time.sleep(.05)
    '''
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
    '''


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
