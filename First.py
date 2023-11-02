import pyautogui as ag

import time

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

    def drag(self,horiz,vert,duration,button):

        if button=='l':
            button='left'
        if button=='r':
            button='right'
        ag.dragTo(horiz,vert, button=button,duration=duration)

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

    def moveMouseNEW(self, time, shift, duration=1):
        # This cool function simple takes the time (time of day eg, 3 pm) and the shift (eg: 1st shift) and
             # duration of mouse move, and the mouse will go to that spot. No more need to specify pixels
        # Vertical pixel difference between shifts: 50px

        shift = shift - 1  # decrement by one to get correct results
        shiftDiff = 52  # pixel distance between shifts (adjust this if mouse is not accurante
        tBase = 524  # base value for time which is 8 am (horizontal axis)
        sBase = 351  # base value for shift which is the top shift showing on screen (vertical axis)

        timeUnit = 30  # number of pixels for a time unit (set at 30 mins;ie 38px = 30 mins of time)

        timeSteps = self.timeSteps(time)  # number of time steps from base (8am) to desired time

        vert = sBase + (
                    shift * shiftDiff)  # get shift pixel value multiply base value with number of shifts downwards on screen
        horiz = tBase + (timeSteps * timeUnit)

        ag.moveTo(horiz, vert, duration)

    def eraser(self):
        '''
        select the eraser function from side pane
        inputs: none
        '''
        self.moveMouse(22,462,0.5,'y') # click eraser selection button

    def otf(self):
        '''
        select the otf activity function from side pane
        inputs: none
        '''
        self.moveMouse(24,427,0.5,'y') #open activity pane
        self.moveMouse(66,813,0.5,'y') # select otf from list

    def confirmElement(self, image, sector):

        '''
        Confirms if a given element is present on the screen.
        input: image: str of image to search for in the screen ('image.png')
        input: sector: str defining which sector of screen to search for desired element
        output: True if and when the element (the image sent in) is found
        '''

        if sector == 'c':  # Centre Section: set screenshot region for small box in centre of the screen
            regValues = (756, 410, 400, 400)

        loop = True
        while loop:

            if ag.locateOnScreen(image, region=regValues) == None:
                continue
            else:
                loop = False

        return True
    def confirmElementCol(self,x,y,colour):

        '''
        Confirms an element is present by matching a colour expected to a colour on the screen
        :param x: x coordinate of position of colour
        :param y: y coordinate of position of colour
        :param colour: a tuple (r,g,b) given in parantheses
        :return: True once the colour is detected
        '''

        loop = True
        while loop:
            # use eyedroper in Firefox browser options to get colour then convert to rgb
            if ag.pixelMatchesColor(x,y, colour) == False: # colour must be sent as tuple (r,g,b)
                continue
            else:
                loop = False

        return True


# funcList = [moveMouse(706,1052,1,'y')]
#
# for func in funcList:
#     func

def main():

    print('\nEnsure bookmarks bar is on')

    taskSet1=TaskSet() # Scheduling for LA and Pages
    taskSet2=TaskSet() # Sharepoint calendar
    taskSet3=TaskSet() # Calendar for week of scheduling
    taskSet4=TaskSet() # Dayforce for current day
    taskSet5=TaskSet() # Open Email

    taskSet1.moveMouse(605, 1056, 1, 'y')  # go to Firefox (5 position on taskbar)
    time.sleep(2) # delay for first case scenerio; more time needed to open Firefox
    taskSet1.moveMouse(305, 64, 0.2, 'y')  # click to focus address bar (incase not focused)
    # taskSet1.pressKeys('ctrl', 't')  # open new tab (try to add delay here)
    taskSet1.type('dayforcehcm.com', 'y')  # Go to site (consider adding click to addre. bar to ensure cursor)
    if taskSet1.confirmElementCol(665, 575, (48, 103, 219)):
        taskSet1.moveMouse(1226, 640, 0.25, 'y')  # go to autofill user name; Firefox should auto pop this up
    taskSet1.moveMouse(1226, 737, 0.2, 'y')  # go to Login

    if taskSet1.confirmElement('SelectRole.png','c'):
        taskSet1.moveMouse(915, 548, 0.5, 'y')  # select Daily Scheduler (small box before sched loaded) !if this is missed the next function will not be available (shedule button)
    taskSet1.moveMouse(1007, 660, 0.2, 'y')  # click next (on small box)
    taskSet1.moveMouse(1056, 337, 3, 'y')  # click schedule (main button to load sched)
    taskSet1.moveMouse(246,223,6,'y') # click Filter button
    taskSet1.moveMouse(376,261,0.5,'y') # click filter input bar
    taskSet1.moveMouse(410,310,0.5,'y') # select LA
    taskSet1.moveMouse(1629,301,0.2,'y') # click Apply button
    taskSet1.moveMouse(1087, 188, 0.5, 'y')  # open calendar

    # Open a second instance of Dayforce
    taskSet1.pressKeys('ctrl', 't')  # open new tab (try to add delay here)
    taskSet1.type('dayforcehcm.com', 'y')  # Go to site
    if taskSet1.confirmElementCol(665, 575, (48, 103, 219)):
        taskSet1.moveMouse(1226, 640, 0.25, 'y')  # go to autofill user name; Firefox should auto pop this up
    taskSet1.moveMouse(1226, 737, 0.2, 'y')  # go to Login
    if taskSet1.confirmElement('SelectRole.png', 'c'):
        taskSet1.moveMouse(915, 548, 0.5,'y')  # select Daily Scheduler (small box before sched loaded) !if this is missed the next function will not be available (shedule button)
    taskSet1.moveMouse(1007, 660, 0.2, 'y')  # click next (on small box)
    taskSet1.moveMouse(1056, 337, 2, 'y')  # click schedule (main button to load sched)
    taskSet1.moveMouse(246, 223, 5, 'y')  # click Filter button
    taskSet1.moveMouse(376, 261, 0.5, 'y')  # click filter input bar
    taskSet1.moveMouse(396, 390, 0.5, 'y')  # select Page
    taskSet1.moveMouse(1629, 301, 0.2, 'y')  # click Apply button
    taskSet1.moveMouse(1087, 188, 0.5, 'y')  # open calendar

    # Open Sharepoint
    taskSet2.pressKeys('ctrl', 't')  # open new tab
    taskSet2.moveMouse(53, 97, 1, 'y')  # click Sharepoint (on bookmarks tab)
    if taskSet2.confirmElementCol(215, 133, (56, 00, 00)):
        taskSet2.moveMouse(21, 134, 0.5, 'y')  # click Sharepoint menu button (left side)
    taskSet2.moveMouse(88, 447, 2, 'y')  # open calendar
    taskSet2.moveMouse(702,20,1,'y')

    # Open Sharepoint
    taskSet3.pressKeys('ctrl', 't')  # open new tab
    taskSet3.moveMouse(53, 97, 1, 'y')  # click Sharepoint
    if taskSet3.confirmElementCol(215, 133, (56, 00, 00)):
        taskSet3.moveMouse(21, 134, 0.5, 'y')  # click Sharepoint menu button (left side)
    taskSet3.moveMouse(88, 447, 2, 'y')  # open calendar
    taskSet3.moveMouse(572, 269, 1, 'y')  # open date selection calendar
    taskSet3.moveMouse(926, 22, 1, 'y')  # open calendar

    taskSet3.moveMouse(828, 22, 1, 'y')  # open calendar
    taskSet3.drag(-1107,18,1,'l') # drag calendar to left screen

    # Open last instance of Dayforce for current day
    taskSet4.moveMouse(173, 68, 1, 'y')  # click on blank area of browser to focus the browser
    taskSet4.pressKeys('ctrl', 't')  # open new tab (try to add delay here)
    taskSet4.type('dayforcehcm.com', 'y')  # Go to site
    if taskSet1.confirmElementCol(665, 575, (48, 103, 219)):
        taskSet4.moveMouse(1226, 640, 0.25, 'y')  # go to autofill user name; Firefox should auto pop this up
    taskSet4.moveMouse(1226, 737, 0.2, 'y')  # go to Login
    if taskSet4.confirmElement('SelectRole.png', 'c'):
        taskSet4.moveMouse(915, 548, 0.5,'y')  # select Daily Scheduler (small box before sched
    taskSet4.moveMouse(1007, 660, 0.2, 'y')  # click next (on small box)
    taskSet4.moveMouse(1056, 337, 3, 'y')  # click schedule (main button to load sched)
    taskSet4.moveMouse(246, 223, 6, 'y')  # click Filter button
    taskSet4.moveMouse(376, 261, 0.5, 'y')  # click filter input bar
    taskSet4.moveMouse(410, 310, 0.5, 'y')  # select LA
    taskSet4.moveMouse(1629, 301, 0.2, 'y')  # click Apply button
    taskSet4.moveMouse(1087, 188, 0.5, 'y')  # open calendar

    # Open Email
    taskSet5.pressKeys('ctrl', 't')  # open new tab
    taskSet5.moveMouse(53, 97, 1, 'y')  # click Sharepoint (on bookmarks tab)
    if taskSet5.confirmElementCol(215, 133, (56, 00, 00)):
        taskSet5.moveMouse(21, 134, 0.5, 'y')  # click Sharepoint menu button (left side)
    taskSet5.moveMouse(83, 254, 2, 'y')  # open email (Outlook)









main()





# moveMouse(1226,607,3,'y') # go to user name
#
# type('andswi','n') # Go to site
#
# moveMouse(1226,683,1,'y') # go to Pass


