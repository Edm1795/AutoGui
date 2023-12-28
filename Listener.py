

from pynput.mouse import Listener

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

        baseTime=8

        return (desiredTime-baseTime)*2

    def moveMouseNEW(self,time,shift,duration=1):

        tBase=720 # base value for time which is 8 am (horizontal axis)
        sBase=481 # base value for shift which is the top shift showing on screen (vertical axis)

        timeUnit=38 #number of pixels for a time unit (set at 30 mins;ie 38px = 30 mins of time)

        timeSteps=self.timeSteps(time) # number of time steps from base (8am) to desired time


        if shift==1:
            vert=sBase

        horiz=tBase+(timeSteps*timeUnit)


        ag.moveTo(horiz,vert,duration)

    def click(self):
        '''
        Clicks the mouse
        '''
        ag.click()

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

task1=TaskSet()
def on_move(x, y):
    print ("Mouse moved")

def on_click(x, y, button, pressed,task=task1):
    print ("Mouse clicked")
    task1.drag(300,500,2,'l')

def on_scroll(x, y, dx, dy):
    print ("Mouse scrolled")



with Listener(on_click=on_click) as listener:
    listener.join()
