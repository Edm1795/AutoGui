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

        baseTime=8

        # Handling the case for 9pm input (an exception) Note: can not mix int and string in inputs
        # if str(desiredTime[1]).lower()=='p':
        #     return ((desiredTime - baseTime)+13) * 2
        # else:
        if len(str(desiredTime))<3: # if input into function is 8,9,10,11,12; anything without a half hour (eg,830)
            return (desiredTime-baseTime)*2 # Returns number of 30 min blocks from baseTime
        else:
            return ((desiredTime-baseTime)*2)+1 # Returns number of 30 min blocks if a half hour is desired (eg 9:30)


    def moveMouseNEW(self,time,shift,duration=1):

        # Start values for home com
        # tBase=720 # base value for time which is 8 am (horizontal axis)
        # sBase=481 # base value for shift which is the top shift showing on screen (vertical axis)
        # timeUnit = 38  # number of pixels for a time unit (set at 30 mins;ie 38px = 30 mins of time)
        # shiftUnit = 32  # Number of pixels between adjacent shifts (top shift and next one below)

        tBase = 524  # base value for time which is 8 am (horizontal axis)
        sBase = 380  # base value for shift which is the top shift showing on screen (vertical axis)

        timeUnit=30 #number of pixels for a time unit (set at 30 mins;ie 38px = 30 mins of time)
        shiftUnit=51 # Number of pixels between adjacent shifts (top shift and next one below)
        timeSteps=self.timeSteps(time) # number of time steps from base (8am) to desired time


        if shift==1: # if targeting first shift set vert to base value
            vert=sBase
        else: # if target is any other shift set to base * the number of shifts down
            vert=sBase + (shiftUnit * (shift-1))

        horiz=tBase+(timeSteps*timeUnit) # Set hoirz to time base * number of hours forward
        # eg: 8am+(2 timesteps*38pixels) Note: one time step = 30 mins not 1 hour.


        ag.moveTo(horiz,vert,duration)

    def click(self):
        '''
        Clicks the mouse
        '''
        ag.click()

    def drag(self,vert,horiz,duration=1,button='l'):

        if button=='l':
            button='left'
        if button=='r':
            button='right'
        ag.dragTo(vert, horiz, button=button,duration=duration)

    def dragNEW(self,time,shift,duration,button):
        # Start values for home com
        # tBase=720 # base value for time which is 8 am (horizontal axis)
        # sBase=481 # base value for shift which is the top shift showing on screen (vertical axis)
        # timeUnit = 38  # number of pixels for a time unit (set at 30 mins;ie 38px = 30 mins of time)
        # shiftUnit = 32  # Number of pixels between adjacent shifts (top shift and next one below)

        tBase = 524  # base value for time which is 8 am (horizontal axis)
        sBase = 380  # base value for shift which is the top shift showing on screen (vertical axis)

        timeUnit=30 #number of pixels for a time unit (set at 30 mins;ie 38px = 30 mins of time)
        shiftUnit=51 # Number of pixels between adjacent shifts (top shift and next one below)
        timeSteps=self.timeSteps(time) # number of time steps from base (8am) to desired time

        if button=='l':
            button='left'
        if button=='r':
            button='right'

        if shift==1: # if targeting first shift set vert to base value
            vert=sBase
        else: # if target is any other shift set to base * the number of shifts down
            vert=sBase + (shiftUnit * (shift-1))

        horiz=tBase+(timeSteps*timeUnit) # Set hoirz to time base * number of hours forward
        # eg: 8am+(2 timesteps*38pixels) Note: one time step = 30 mins not 1 hour.


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

    taskSet1=TaskSet()

    # taskSet1.moveMouse(29, 463, 0.5, 'y')  # click activity button, left side pane
    # taskSet1.moveMouse(80, 792, 1, 'y')  # click 'Lists'
    taskSet1.moveMouse(985,654,1,'y')
    for num in range(1, 2):
        taskSet1.pressKeys('ctrl', str(num))

        taskSet1.moveMouseNEW(1,3)
        taskSet1.dragNEW(2,3,'l')  # drag lists to 9:30 am


    # taskSet1.moveMouseNEW(8,1)
    # time.sleep(0.3)
    # taskSet1.moveMouseNEW(8,2)
    # time.sleep(0.3)
    # taskSet1.moveMouseNEW(9,2)

main()
