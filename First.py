# Change timings to variables, also possibly make global function controlling timings which can set the whole programs
# I think browser needs to be at 120%
import pyautogui as ag
import time
import datetime

class TaskSet:
    '''
    Class for a single unified set of automated GUI movements and actions
    '''
    def __init__(self):

        self.LA = (478, 309) # vals for work com: (478, 309); vals for home (553, 391) set x,y coordinates of LA in Filter Drop Down menu
        self.Page = (406, 412) # set x,y coordinates of Page in Filter Drop Down menu
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
        Inputs: letters (str): a sequence of letters or numbers to be typed
        Enter: a str 'y' or 'no', if you want to press the enter key after inputing letters
        '''
        ag.write(letters)

        if enter == 'y':
            time.sleep(0.5) # used to add gap between text input and pressing enter
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

    def clickDate(self):

        '''
        This function gets the current date and then calculates the position of that date on the drop down calendar and clicks it.
        It contains the helper functions called week() which gathers the week number a certain date is in, ex week 1, week 2
        and another called weekdayConver() which converts pythons .weekday() function to the needed values for this program
        '''

        def weekdayConver(curDate):
            '''
            Convert the normal return values of .weekday() to the needed values for this program where Sunday must be 0,
            Monday 1...
            :param curDate: Obj of the current date or any date you choose to input
            :return: int for each day of the week with Sun as 0
            '''

            day = curDate.weekday()  # extract the weekday int from the datetime object

            if day == 6:
                return 0
            if day == 5:
                return 6
            if day == 4:
                return 5
            if day == 3:
                return 4
            if day == 2:
                return 3
            if day == 1:
                return 2
            if day == 0:
                return 1

        def week():  # date=curDate.day, year=curDate.year, month=curDate.month
            '''
            This function determines the week number within a month a given date resides. For example which week is Dec.
            14th.
            :param date:  int, current date
            :param year: int current year
            :param month: int current month
            :return: int, the week a given date resides eg: 1,2,3,4,5
            '''
            # Create a date object
            dateObj = datetime.date.today()  # (year, month, date)

            # Calculate the week number within the month
            first_day_of_month = dateObj.replace(day=1)  # Get the first day of the month
            offset = (
                                 first_day_of_month.weekday() - 6) % 7  # Calculate the offset for Sunday as the first day of the week
            adjusted_date = first_day_of_month - datetime.timedelta(days=offset)  # Adjust the date to start on a Sunday
            week_number = (dateObj - adjusted_date).days // 7 + 1  # Calculate the week number

            return week_number

        curDate = datetime.date.today()  # get date object for current day; datetime.date.today() gives all three values ymd
        day = weekdayConver(
            curDate)  # extract the weekday from the current date object as an int 0-6 for Mon-Sat. This is done with a helper func.
        print(day)
        print(week())
        yDiff = 32  # number of pixels between adjacent rows (eg week 1 - week 2) (work 32, home 37)
        xDiff = 36  # number of pixels between immediately adjacent days of week (eg:mon-tues) (work 36, home 44)
        xDefault = 851  # 36 pixel difference (work 851, home com 857)
        yDefault = 301  # (work 301, home com 381)

        x = xDefault + (day * xDiff)

        if week() == 1:
            y = yDefault  # if needed the first week of the month supply only the yDefault
        else:  # if needing other weeks, subtract 1 and mulitply by the yDiff (pixel difference) week 2 = (2-1)*yDiff
            y = yDefault + ((week() - 1) * yDiff)
        print(x, y)
        self.moveMouse(x,y,1,'y')

    def getLACoord(self):
        return self.LA

class CheckForElem:

    '''
    Class for checking given elements are present on the screen. For example checks if a certain word is present
    or a certain colour of pixel
    '''

    def __init__(self):
        pass

    def confirmImage(self, image, sector, topLeftx=0, topLefty=0, bottomRightx=0, bottomRighty=0):

        '''
        Confirms if a given element is present on the screen.
        input: image: str of image to search for in the screen ('image.png')
        inputs: sector: str defining which sector of screen to search for desired element
            Exact values of box to check for element (if not using a general sector of the screen
        output: True if and when the element (the image sent in) is found
        '''

        if sector == 'c':  # Centre Section: set screenshot region for small box in centre of the screen
            regValues = (756, 410, 400, 400)
        if sector == 'cr': # Screenshot for centre right
            regValues = (1000, 380, 500, 500)
        if sector == 'n':  # If no sector is used, load in exact values of box to check for element
            regValues = (topLeftx, topLefty, bottomRightx, bottomRighty)

        loop = True
        while loop:

            if ag.locateOnScreen(image, region=regValues) == None:
                continue
            else:
                loop = False

        return True

    def confirmColour(self, x, y, colour):

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
            if ag.pixelMatchesColor(x, y, colour) == False:  # colour must be sent as tuple (r,g,b)
                continue
            else:
                loop = False
        time.sleep(0.1)
        return True


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

    def getFast(self):
        return self.fast

    def getMed(self):
        return self.med

    def getSlow(self):
        return self.slow

# funcList = [moveMouse(706,1052,1,'y')]
#
# for func in funcList:
#     func

def main():

    print('\nEnsure bookmarks bar is on','\nAlso browser probably needs to be at 120%')

    taskSet1=TaskSet() # Scheduling for LA and Pages
    taskSet2=TaskSet() # Sharepoint calendar
    taskSet3=TaskSet() # Calendar for week of scheduling
    taskSet4=TaskSet() # Dayforce for current day
    taskSet5=TaskSet() # Open Email
    checkForElem = CheckForElem()
    timeVal=TimeValues('f') # Instantiate TimeValues to fast

    taskSet1.moveMouse(605, 1056, 0.5, 'y')  # go to Firefox (5 position on taskbar)
    time.sleep(1) # delay for first case scenerio; more time needed to open Firefox
    taskSet1.moveMouse(305, 64, timeVal.getFast(), 'y')  # click to focus address bar (incase not focused)
    # taskSet1.pressKeys('ctrl', 't')  # open new tab (try to add delay here)
    taskSet1.type('dayforcehcm.com', 'y')  # Go to site (consider adding click to addre. bar to ensure cursor)
    if checkForElem.confirmColour(665,575, (48,103,219)):
        taskSet1.moveMouse(1226, 640, timeVal.getMed(), 'y')  # go to autofill user name; Firefox should auto pop this up
    taskSet1.moveMouse(1226, 737, timeVal.getMed(), 'y')  # go to Login
    if checkForElem.confirmImage('SelectRole.png','c'):  # monitor for when Select Role box displays then select Daily Scheduler (tiny radio button)
        taskSet1.moveMouse(915, 548, timeVal.getMed(), 'y')  # select Daily Scheduler (small box before sched loaded) !if this is missed the next function will not be available (shedule button)
    taskSet1.moveMouse(1007, 660, timeVal.getFast(), 'y')  # click next (on small box)
    if checkForElem.confirmImage('Schedules.png','n',1007,370,1113,397):
        taskSet1.moveMouse(1056, 337, timeVal.getMed(), 'y')  # click schedule (main button to load sched)
    if checkForElem.confirmColour(227, 223, (28, 68, 156)):  # Check for filter button by colour of icon
        taskSet1.moveMouse(246, 223, timeVal.getMed(), 'y')  # click Filter button
    taskSet1.moveMouse(376,261,timeVal.getFast(),'y') # click filter input bar
    taskSet1.moveMouse(taskSet1.getLACoord()[0], taskSet1.getLACoord()[1],timeVal.getFast(),'y') # select LA
    taskSet1.moveMouse(1629,301,timeVal.getFast(),'y') # click Apply button
    taskSet1.moveMouse(1087, 188, timeVal.getSlow(), 'y')  # open calendar

    # Open a second instance of Dayforce
    taskSet1.pressKeys('ctrl', 't')  # open new tab (try to add delay here)
    taskSet1.type('dayforcehcm.com', 'y')  # Go to site
    if checkForElem.confirmColour(665, 575, (48, 103, 219)):
        taskSet1.moveMouse(1226, 640, 0.25, 'y')  # go to autofill user name; Firefox should auto pop this up
    taskSet1.moveMouse(1226, 737, 0.2, 'y')  # go to Login
    if checkForElem.confirmImage('SelectRole.png','c'):  # monitor for when Select Role box displays then select Daily Scheduler (tiny radio button)
        taskSet1.moveMouse(915, 548, 0.2, 'y')  # select Daily Scheduler (small box before sched loaded) !if this is missed the next function will not be available (shedule button)
    taskSet1.moveMouse(1007, 660, 0.2, 'y')  # click next (on small box)
    if checkForElem.confirmImage('Schedules.png', 'n', 1007, 370, 1113, 397):
        taskSet1.moveMouse(1056, 337, 0.25, 'y')  # click schedule (main button to load sched)
    if checkForElem.confirmColour(227, 223, (28, 68, 156)):  # Check for filter button by colour of icon
        taskSet1.moveMouse(246, 223, 0.2, 'y')  # click Filter button
    taskSet1.moveMouse(376, 261, 0.2, 'y')  # click filter input bar
    taskSet1.moveMouse(476, 411, 0.2, 'y')  # select Page
    taskSet1.moveMouse(1629, 301, 0.2, 'y')  # click Apply button
    taskSet1.moveMouse(1087, 188, 0.5, 'y')  # open calendar

    # Open Sharepoint
    taskSet2.pressKeys('ctrl', 't')  # open new tab
    taskSet2.moveMouse(53, 97, 0.2, 'y')  # click Sharepoint (on bookmarks tab)
    if checkForElem.confirmColour(215, 133, (56, 00, 00)):
        taskSet2.moveMouse(21, 134, 0.2, 'y')  # click Sharepoint menu button (left side)
    if checkForElem.confirmImage('Calendar.png', 'n', 25, 428, 65, 467):
        taskSet2.moveMouse(88, 447, 0.2, 'y')  # open calendar
    taskSet2.moveMouse(702,20,1,'y')

    # Open Sharepoint
    taskSet3.pressKeys('ctrl', 't')  # open new tab
    taskSet3.moveMouse(53, 97, 0.2, 'y')  # click Sharepoint
    if checkForElem.confirmColour(215, 133, (56, 00, 00)):
        taskSet3.moveMouse(21, 134, 0.2, 'y')  # click Sharepoint menu button (left side)
    if checkForElem.confirmImage('Calendar.png', 'n', 25, 428, 65, 467):
        taskSet3.moveMouse(88, 447, 0.2, 'y')  # open calendar
    taskSet3.moveMouse(572, 269, 1, 'y')  # open date selection calendar
    taskSet3.moveMouse(926, 22, 1, 'y')  # open calendar

    taskSet3.moveMouse(828, 22, 1, 'y')  # open calendar
    taskSet3.drag(-1107,18,0.5,'l') # drag calendar to left screen

    # Open last instance of Dayforce for current day
    taskSet4.moveMouse(173, 68, 1, 'y')  # click on blank area of browser to focus the browser
    taskSet4.pressKeys('ctrl', 't')  # open new tab (try to add delay here)
    taskSet4.type('dayforcehcm.com', 'y')  # Go to site
    if checkForElem.confirmColour(665, 575, (48, 103, 219)):
        taskSet4.moveMouse(1226, 640, 0.25, 'y')  # go to autofill user name; Firefox should auto pop this up
    taskSet1.moveMouse(1226, 737, 0.2, 'y')  # go to Login
    if checkForElem.confirmImage('SelectRole.png','c'):  # monitor for when Select Role box displays then select Daily Scheduler (tiny radio button)
        taskSet4.moveMouse(915, 548, 0.2,'y')  # select Daily Scheduler (small box before sched loaded) !if this is missed the next function will not be available (shedule button)
    taskSet1.moveMouse(1007, 660, 0.2, 'y')  # click next (on small box)
    if checkForElem.confirmImage('Schedules.png', 'n', 1007, 370, 1113, 397):
        taskSet4.moveMouse(1056, 337, 0.25, 'y')  # click schedule (main button to load sched)
    if checkForElem.confirmColour(227, 223, (28, 68, 156)):  # Check for filter button by colour of icon
        taskSet4.moveMouse(246, 223, 0.2, 'y')  # click Filter button
    taskSet4.moveMouse(376, 261, 0.2, 'y')  # click filter input bar
    taskSet4.moveMouse(taskSet4.getLACoord()[0], taskSet4.getLACoord()[1], 0.2, 'y')  # select LA
    taskSet4.moveMouse(1629, 301, 0.2, 'y')  # click Apply button
    taskSet4.moveMouse(1087, 188, 0.5, 'y')  # open calendar
    taskSet4.clickDate()  # find the current date on the calendar and click it

    # Open Email
    taskSet5.pressKeys('ctrl', 't')  # open new tab
    taskSet5.moveMouse(53, 97, timeVal.getFast(), 'y')  # click Sharepoint (on bookmarks tab)
    if checkForElem.confirmColour(215, 133, (56, 00, 00)):
        taskSet5.moveMouse(21, 134, 0.2, 'y')  # click Sharepoint menu button (left side)
    if checkForElem.confirmImage('Calendar.png', 'n', 25, 428, 65, 467):
        taskSet5.moveMouse(83, 254, 0.2, 'y')  # open email (Outlook)

    print('Complete.')

main()





# moveMouse(1226,607,3,'y') # go to user name
#
# type('andswi','n') # Go to site
#
# moveMouse(1226,683,1,'y') # go to Pass


