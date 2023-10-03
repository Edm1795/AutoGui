import time

import pyautogui as ag

class TaskSet:
    '''
    Class for a single unified set of automated GUI movements and actions
    '''
    def __init__(self):

        pass
    def moveMouse(self,horiz,vert,time,click):
        '''
        Inputs: int: horizontal and vertical position where the mouse must end up
        Time: int: mount of time to take to get pointer to its position
        click: a str value of 'y' if a click is desired at final position
        '''
        ag.moveTo(horiz, vert, duration=time)

        if click == 'y':
            ag.click()
        else:
            pass

    def timeSteps(self,desiredTime):

        '''
        method returns the number of time steps between basetime (8am) and desired time
        input: desiredTime int, the time you want to go to
        output: int, number of units from basetime (8am) to desired time measured in 30 min incr.
        eg: 9 am is two time steps forward from basetime (8am) (two half hour units)
        '''

        if desiredTime>0 and desiredTime<8: # If any time is between 1 and 7 add 12 hours. Eg 1 --> 13; 13 = 1 pm
            desiredTime=desiredTime+12

        baseTime=8

        return (desiredTime-baseTime)*2

    def moveMouseNEW(self,time,shift,duration=1):

        #Vertical pixel difference between shifts: 50px

        shift = shift-1 # decrement by one to get correct results
        shiftDiff=52 # pixel distance between shifts (adjust this if mouse is not accurante
        tBase=524 # base value for time which is 8 am (horizontal axis)
        sBase=351 # base value for shift which is the top shift showing on screen (vertical axis)

        timeUnit=30 #number of pixels for a time unit (set at 30 mins;ie 38px = 30 mins of time)

        timeSteps=self.timeSteps(time) # number of time steps from base (8am) to desired time

        vert=sBase+(shift*shiftDiff) # get shift pixel value multiply base value with number of shifts downwards on screen
        horiz=tBase+(timeSteps*timeUnit)


        ag.moveTo(horiz,vert,duration)

    def click(self):
        '''
        Clicks the mouse
        '''
        ag.click()

    def dragNEW(self,time,shift,button,duration=1):

        if button=='l':
            button='left'
        if button=='r':
            button='right'

        shift = shift - 1  # decrement by one to get correct results
        shiftDiff = 52  # pixel distance between shifts (adjust this if mouse is not accurante
        tBase = 524  # base value for time which is 8 am (horizontal axis)
        sBase = 351  # base value for shift which is the top shift showing on screen (vertical axis)

        timeUnit = 30  # number of pixels for a time unit (set at 30 mins;ie 38px = 30 mins of time)

        timeSteps = self.timeSteps(time)  # number of time steps from base (8am) to desired time

        vert = sBase + (shift * shiftDiff)  # get shift pixel value multiply base value with number of shifts downwards on screen
        horiz = tBase + (timeSteps * timeUnit)

        ag.dragTo(horiz,vert, button=button,duration=duration)

    def drag(self,vert,horiz,duration,button):

        if button=='l':
            button='left'
        if button=='r':
            button='right'
        ag.dragTo(vert, horiz, button=button,duration=duration)

    def pressKeys(self,holdKey,secondKey):

        '''
        Double key press function: eg, ctrl + a
        Inputs: holdKey: str key to hold down, eg: ctrl or shift
        secondKey:  str second key to press eg, a
        '''
        ag.keyDown(holdKey)  # hold down the shift key
        ag.press(secondKey)  # press the left arrow key
        ag.keyUp(holdKey)

    def type(self,letters,enter):
        '''
        Types keyboard input to the cursor.
        Inputs: letters: a sequence of strings to be typed
        Enter: a str 'y' or 'no', if you want to press the enter key after inputing letters
        '''
        ag.write(letters)

        if enter == 'y':
            ag.press('enter')


# funcList = [moveMouse(706,1052,1,'y')]
#
# for func in funcList:
#     func

def main():

    # taskSet1=TaskSet()
    # taskSet1.moveMouse(967,91,1,'n')
    # taskSet1.drag(820,91,2,'l')
    # taskSet1.moveMouse(706,1052,1,'y')
    # taskSet1.pressKeys('ctrl', 't')  # open new tab
    # taskSet1.type('dayforcehcm.com', 'y')  # Go to site
    # taskSet1.moveMouse(1315, 917, 3, 'y')  # click login
    # taskSet1.moveMouse(315, 432, 8, 'y')  # go to schedule
    # taskSet1.moveMouse(985, 241, 6, 'y')  # open calendar

    # taskSet1.moveMouse(589,243,1,'y')
    # for num in range(1,8):
    #     taskSet1.pressKeys('ctrl',str(num))
    #     time.sleep(1)
    #     taskSet1.moveMouse(589, 243, 1, 'y')
    # taskSet1.moveMouse(600,474,0.5,'y')
    #
    # taskSet1.moveMouse(655,474,0.5,'n')
    # taskSet1.drag(767,474,2,'l')
    #
    # ag.dragTo(100, 200, 2,button='left')
    # ag.moveTo(400,400)
    # ag.drag(100, 200, 2,button='left')

    # taskSet1.moveMouseNEW(8,1)
    # taskSet1.moveMouseNEW(9,1)
    # taskSet1.moveMouseNEW(8,2)
    # taskSet1.moveMouseNEW(9,2)
    # taskSet1.moveMouseNEW(9, 3)
    # taskSet1.moveMouseNEW(9, 4)
    # taskSet1.moveMouseNEW(10,4)
    #
    # # taskSet1.moveMouseNEW(11,5)
    # taskSet1.moveMouseNEW(1,1)
    # taskSet1.moveMouseNEW(2, 1)
    # taskSet1.moveMouseNEW(3, 1)
    # taskSet1.moveMouseNEW(4, 2)
    # taskSet1.moveMouseNEW(5, 1)
    # taskSet1.moveMouseNEW(6, 1)
    # taskSet1.moveMouseNEW(7, 1)
    # taskSet1.moveMouseNEW(8, 1)

    # taskSet1.moveMouseNEW(2,6)
    # taskSet1.dragNEW(3,6,'l')

    # taskSet1.moveMouseNEW(3, 2)
    # taskSet1.dragNEW(4, 2, 'l')

    # taskSet1.moveMouseNEW(4, 3)
    # taskSet1.dragNEW(5, 3, 'l')

### Set up desktop for scheduling  ###
    taskSet1=TaskSet() # Scheduling for LA and Pages
    taskSet2=TaskSet() # Sharepoint calendar
    taskSet3=TaskSet() # Calendar for week of scheduling
    taskSet4=TaskSet() # Dayforce for current day

    taskSet1.moveMouse(605, 1056, 1, 'y')  # go to Firefox
    time.sleep(2) # delay for first case scenerio; more time needed to open Firefox
    # taskSet1.pressKeys('ctrl', 't')  # open new tab (try to add delay here)
    taskSet1.type('dayforcehcm.com', 'y')  # Go to site
    taskSet1.moveMouse(1226, 640, 3, 'y')  # go to autofill user name; Firefox should auto pop this up
    taskSet1.moveMouse(1226, 737, 1, 'y')  # go to Login
    taskSet1.moveMouse(915, 548, 7, 'y')  # select Daily Scheduler (small box before sched loaded) !if this is missed the next function will not be available (shedule button)
    taskSet1.moveMouse(1007, 660, 1, 'y')  # click next (on small box)
    taskSet1.moveMouse(1056, 337, 3, 'y')  # click schedule (main button to load sched)
    taskSet1.moveMouse(246,223,6,'y') # click Filter button
    taskSet1.moveMouse(376,261,0.5,'y') # click filter input bar
    taskSet1.moveMouse(410,310,0.5,'y') # select LA
    taskSet1.moveMouse(1629,301,0.5,'y') # click Apply button
    taskSet1.moveMouse(1087, 188, 1, 'y')  # open calendar

    # Open a second instance of Dayforce
    taskSet1.pressKeys('ctrl', 't')  # open new tab (try to add delay here)
    taskSet1.type('dayforcehcm.com', 'y')  # Go to site
    taskSet1.moveMouse(1226, 640, 3, 'y')  # go to autofill user name; Firefox should auto pop this up
    taskSet1.moveMouse(1226, 737, 1, 'y')  # go to Login
    taskSet1.moveMouse(915, 548, 7, 'y')  # select Daily Scheduler (small box before sched loaded)
    taskSet1.moveMouse(1007, 660, 1, 'y')  # click next (on small box)
    taskSet1.moveMouse(1056, 337, 2, 'y')  # click schedule (main button to load sched)
    taskSet1.moveMouse(246, 223, 5, 'y')  # click Filter button
    taskSet1.moveMouse(376, 261, 0.5, 'y')  # click filter input bar
    taskSet1.moveMouse(396, 390, 0.5, 'y')  # select Page
    taskSet1.moveMouse(1629, 301, 0.5, 'y')  # click Apply button
    taskSet1.moveMouse(1087, 188, 1, 'y')  # open calendar

    # Open Sharepoint
    taskSet2.pressKeys('ctrl', 't')  # open new tab
    taskSet2.moveMouse(53, 97, 1, 'y')  # click Sharepoint
    taskSet2.moveMouse(21, 134, 5, 'y')  # click Sharepoint menu button (left side)
    taskSet2.moveMouse(88, 447, 2, 'y')  # open calendar
    taskSet2.moveMouse(702,20,1,'y')

    # Open Sharepoint
    taskSet3.pressKeys('ctrl', 't')  # open new tab
    taskSet3.moveMouse(53, 97, 1, 'y')  # click Sharepoint
    taskSet3.moveMouse(21, 134, 1, 'y')  # click outlook menu button (left side)
    taskSet3.moveMouse(88, 447, 2, 'y')  # open calendar
    taskSet3.moveMouse(572, 269, 1, 'y')  # open date selection calendar
    taskSet3.moveMouse(926, 22, 1, 'y')  # open calendar

    taskSet3.moveMouse(828, 22, 1, 'y')  # open calendar
    taskSet3.drag(-1107,18,1,'l') # drag calendar to left screen

    # Open last instance of Dayforce for current day
    taskSet4.moveMouse(173,68,1,'y')
    taskSet4.pressKeys('ctrl', 't')  # open new tab (try to add delay here)
    taskSet4.type('dayforcehcm.com', 'y')  # Go to site
    taskSet4.moveMouse(1226, 640, 3, 'y')  # go to autofill user name; Firefox should auto pop this up
    taskSet4.moveMouse(1226, 737, 1, 'y')  # go to Login
    taskSet4.moveMouse(915, 548, 7, 'y')  # select Daily Scheduler (small box before sched loaded)
    taskSet4.moveMouse(1007, 660, 1, 'y')  # click next (on small box)
    taskSet4.moveMouse(1056, 337, 3, 'y')  # click schedule (main button to load sched)
    taskSet4.moveMouse(246, 223, 6, 'y')  # click Filter button
    taskSet4.moveMouse(376, 261, 0.5, 'y')  # click filter input bar
    taskSet4.moveMouse(410, 310, 0.5, 'y')  # select LA
    taskSet4.moveMouse(1629, 301, 0.5, 'y')  # click Apply button
    taskSet4.moveMouse(1087, 188, 1, 'y')  # open calendar




main()
