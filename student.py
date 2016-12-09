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
    STOP_DIST = 30
    ###### which motor to use to straighten the wheels
    LEFT_SPEED = 90
    RIGHT_SPEED = 90
    ### turn right or left 90
    TIME_PER_DEGREE = 0.011
    TURN_MODIFIER = 1
    turn_track = 0
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
                "5": ("Cruise", self.cruise)

                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        #
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

    ##### Autonomus driving
    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        for x in range(3):
             while True:
            # only if it is clear in front
                if self.isClear():
                    self.cruise()
                if self.isClear():
                    self.cruise()
            # should you backup
                self.watchout()
            # stuck?! choose a better path
                turn_target = self.kenny()
                if turn_target > 0:
                    self.turnR(turn_target)
                else:
                    self.turnL(abs(turn_target))




    ######## Big self driving method
    def cruise(self):
        # Use the GoPiGo API's method to aim the sensor forward
        print("\n----CRUISING----\n")
        servo(self.MIDPOINT)
        # give the robot time to move
        time.sleep(.05)
        # start driving forward
        fwd()
        while True:
            # break the loop if the sensor reading is closer than our stop dist
            reading = us_dist(15)
            if reading < self.STOP_DIST:
                print("---STOPPING CRUISE: " + str(reading) + " CM READING---")
                break
            # YOU DECIDE: How many seconds do you wait in between a check?
            time.sleep(.05)

        # stop if the sensor loop broke
        self.stop()

    ###########watch out, please do not hit the wall, backup!!!!!###########
    def watchout(self):
         if us_dist(15) < 30:
            print("Too close. Backing up for half a second")
            bwd()
            time.sleep(.5)
            self.stop()

    #replacement turn method. Find the best method to turn
    def kenny(self):
        #use the built-in wide scan
        self.wideScan()
        #count will keep track of the contigeous positive readings
        count = 0
        #List of all the open paths we detect
        option = [0]
        SAFETY_BUFFER = 20
        #what increment do you have your widescan set to?
        INC = 2
        ##################################################################################################################################################################################################################
        #####################Build THE OPTIONS
        ##################################################################################################################################################################################################################
        for x in range(self.MIDPOINT - 60, self.MIDPOINT + 60):
            if self.scan[x]:
                # add 30 if you want, this is an extra safety buffer
                if self.scan[x] > (self.STOP_DIST + SAFETY_BUFFER):
                    count += 1
                else:
                    # aww nuts, I have to reset the count, this path won't work
                    count = 0
                # YOU DECIDE: Is 16 degrees the right size to consider as a safe window?
                if count > (16 / INC) - 1:
                    # SUCCESS! I've found enough positive readings in a row
                    print("---FOUND OPTION: from " + str(x - 16) + " to " + str(x))
                    # set the counter up again for next time
                    count = 0
                    # add this option to the list
                    option.append(x - 8)


        ####################################
        ############## PICK FROM THE OPTIONS - experimental
        # The biggest angle away from our midpoint we could possibly see is 90
        bestoption = 90
        # the turn it would take to get us aimed back toward the exit - experimental
        ideal = -self.turn_track
        print("\nTHINKING. Ideal turn: " + str(ideal) + " degrees\n")
        # x will iterate through all the angles of our path options
        for x in option:
            # skip our filler option
            if x != 0:
                # the change to the midpoint needed to aim at this path
                turn = self.MIDPOINT - x
                # state our logic so debugging is easier
                print("\nPATH @  " + str(x) + " degrees means a turn of " + str(turn))
                # if this option is closer to our ideal than our current best option...
                if abs(ideal - bestoption) > abs(ideal - turn):
                    # store this turn as the best option
                    bestoption = turn
        if bestoption > 0:
            print("\nABOUT TO TURN RIGHT BY: " + str(bestoption) + " degrees")
        else:
            print("\nABOUT TO TURN LEFT BY: " + str(abs(bestoption)) + " degrees")
        return bestoption


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
        print("let's turn"+str(self.turn_track) + " degrees away")
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER, self.RIGHT_SPEED * self.TURN_MODIFIER)
        right_rot()
        time.sleep(deg * self.TIME_PER_DEGREE)
        self.stop()
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)

    def turnL(self, deg):
        # blah blah blah
        self.turn_track += deg
        print("let's turn" + str(self.turn_track) + " degrees away")
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER, self.RIGHT_SPEED * self.TURN_MODIFIER)
        #do turn stuff
        left_rot()
        time.sleep(deg * self.TIME_PER_DEGREE)
        self.stop()
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)


    ######## speed method
    def setSpeed(self, left, right):
        print("left speed: " + str(left) + '// "right speed: " '+str(right))
        set_left_speed(int(left))
        set_right_speed(int(right))
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







####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
