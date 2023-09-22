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

def main():

    taskSet1=TaskSet()

    taskSet1.moveMouse(706,1052,1,'y')
    taskSet1.pressKeys('ctrl', 't')  # open new tab
    taskSet1.type('dayforcehcm.com', 'y')  # Go to site
    taskSet1.moveMouse(1315, 917, 3, 'y')  # click login
    taskSet1.moveMouse(315, 432, 8, 'y')  # go to schedule
    taskSet1.moveMouse(985, 241, 6, 'y')  # open calendar

    for num in range(1,8): # switcher for days of the week from Sun to Sat.
        taskSet1.pressKeys('ctrl',str(num)) # hot key for changing days of week

main()

