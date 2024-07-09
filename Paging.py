# Page Lists input (put screen to 120 %)

import pyautogui as ag
import time


class TaskSet:
    '''
    Class for a single unified set of automated GUI movements and actions
    '''

    def __init__(self):

        pass

    def moveMouse(self, horiz, vert, time, click):
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

    def click(self):
        '''
        Clicks the mouse
        '''
        ag.click()

    def drag(self, horiz, vert, duration, button):

        if button == 'l':
            button = 'left'
        if button == 'r':
            button = 'right'
        ag.dragTo(horiz, vert, button=button, duration=duration)

    def pressKeys(self, holdKey, secondKey):

        '''
        Double key press function: eg, ctrl + a
        Inputs: holdKey: str key to hold down, eg: ctrl or shift
        secondKey:  str second key to press eg, a
        '''
        ag.keyDown(holdKey)  # hold down the shift key
        time.sleep(0.25)
        ag.press(secondKey)  # press the left arrow key
        ag.keyUp(holdKey)

    def type(self, letters, enter):
        '''
        Types keyboard input to the cursor.
        Inputs: letters: a sequence of strings to be typed
        Enter: a str 'y' or 'no', if you want to press the enter key after inputing letters
        '''
        ag.write(letters)

        if enter == 'y':
            ag.press('enter')
class TimeValues:
    '''
    A class which holds a variety of time values to use for moving the mouse accross the screen.
    This standardizes the timings for automation and allows for easy alteration of timings across
    the whole program. Upon instantiation you can choose a speed range such as 'f' for fast where all
    values are set to shorter (and thus faster) timings.

    Note: Values have to be calibrated carefully so as to be quick but also not too fast otherwise websites can't handle the speed.

    Inputs: str: 'f' gives all fastest values; 'm' gives medium values; 's' gives slow values
    '''

    def __init__(self, speed):
        if speed == 'f':
            self.fast = 0.1
            self.med = 0.2
            self.slow = 0.3
        if speed == 'm':
            self.fast = 0.2
            self.med = 0.3
            self.slow = 0.4
        if speed == 's':
            self.fast = 0.5
            self.med = 1
            self.slow = 2

    def getFast(self):
        return self.fast

    def getMed(self):
        return self.med

    def getSlow(self):
        return self.slow


def main():
    # taskSet4 = TaskSet()

    # taskSet1.moveMouse(1142,505,1,'y')
    # taskSet1.pressKeys('ctrl', 't')  # open new tab
    # taskSet1.type('dayforcehcm.com', 'y')  # Go to site
    # taskSet1.moveMouse(1315, 917, 3, 'y')  # click login
    # taskSet1.moveMouse(315, 432, 8, 'y')  # go to schedule
    # taskSet1.moveMouse(985, 241, 6, 'y')  # open calendar

    # for num in range(1,8): # switcher for days of the week from Sun to Sat.
    #     taskSet1.pressKeys('ctrl',str(num)) # hot key for changing days of week


    ##### Input Main Tasks for Paging #####

    print('\nset screen zoom to 120% for this program to work! You have 5 seconds. Press ctrl +\nAlso turn off bookmarks bar')
    taskSet1=TaskSet()
    timeVal=TimeValues('s')
    time.sleep(5)

    taskSet1.moveMouse(29, 463, 0.5, 'y')  # click activity button, left side pane
    taskSet1.moveMouse(80, 792, 1, 'y')  # click 'Lists'

    for num in range(1, 8):
        taskSet1.pressKeys('ctrl', str(num))

        taskSet1.moveMouse(630, 406, 1, 'n')  # go to 8 am top shift
        taskSet1.drag(772, 405, 2, 'l')  # drag lists to 10:00 am

        # taskSet1.moveMouse(737, 405, 1, 'l')  # shift previous 9:30 am end over slightly to start new block
        # taskSet1.drag(772, 405, 2, 'l')  # input Lists 9:30 am - 10 am ( no longer needing 30 min block, changing to full 2 hr block given above)

        # Input 2 hour Lists block on 2nd shift
        taskSet1.moveMouse(701, 466, 1, 'n')
        taskSet1.drag(844, 468, 2, 'l')

        # Input 1 hour Lists on third shift\
        taskSet1.moveMouse(773, 528, 1, 'n')
        taskSet1.drag(844, 529, 2, 'l')


main()
