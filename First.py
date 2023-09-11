import pyautogui as ag

def moveMouse(horiz,vert,time,click):
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

def click():
    '''
    Clicks the mouse
    '''
    ag.click()

def pressKeys(holdKey,secondKey):

    '''
    Double key press function: eg, ctrl + a
    Inputs: holdKey: str key to hold down, eg: ctrl or shift
    secondKey:  str second key to press eg, a
    '''
    ag.keyDown(holdKey)  # hold down the shift key
    ag.press(secondKey)  # press the left arrow key
    ag.keyUp(holdKey)

def type(letters,enter):
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

moveMouse(706,1052,1,'y')
# moveMouse(706,1052,1,'y') # open Opera
pressKeys('ctrl','t') # open new tab
# moveMouse(886,79,1)  unnesecary, opera auto places cursor
type('dayforcehcm.com','y') # Go to site
moveMouse(1315,917,3,'y') # click login
moveMouse(315,432,8,'y') # go to schedule
moveMouse(985,241,6,'y') # open calendar
