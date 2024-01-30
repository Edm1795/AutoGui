
import time
from PIL import ImageGrab
import pyautogui as ag

screenshot = ImageGrab.grab()  # Take the screenshot


# ag.screenshot('my_screenshot.png')

class TaskSet:
    '''
    Class for a single unified set of automated GUI movements and actions
    '''

    def __init__(self,computer):

        '''
        initialize values, mostly coordinates of locations on the screen according to what computer you are running the
        program on. Each screen will display important elements of the website in different areas and so the values
        foe each computer must be seperated
        :param computer: str: 'h' for home computer; 'w' for work computer
        '''

        self.progressDict = {}  # Instantiate dictionary which hold keys and values about state of checks on the screen . Eg: {colour: true}

        if computer == 'h': # Initialize values for your home computer
            self.logo=(688, 592) # coordinates of huge "D" on main screen
            self.loginButt=(1315, 917) # coord. of main Login button on main screen
            self.schedRadButt=(938, 547) # coord of Scheduler radio button on first pop up before entering main program
            self.nextButt=(1048,685) # coord of Next button on scheduler pop up window just above
            self.schedIcon=(1116, 422) # largish Schedules icon on top right of screen
            self.filterIcon=(353, 286) # coord of small Filter icon top left for colour check
            self.filterButt=(373, 286) # coord of filter button
            self.filterInputBar=(553, 332) # coord of bar for choosing which positions to filter out for viewing on schedule
            self.LA = (553, 391)  # vals for work com: (478, 309) # Coords for LA role in drop down filter menu
            self.applyButt=(1553, 380) # coords of Apply button on filter menu
            self.monthlyCal=(990, 240) # coords for opening monthly calendar for choosing day to view on screen

        if computer == 'w': # Initialize values for your work computer
            self.logo = (665, 575)  # coordinates of huge "D" on main screen
            self.loginButt = (1226, 737)  # coord. of main Login button on main screen
            self.schedRadButt = (915, 548)  # coord of Scheduler radio button on first pop up before entering main program
            self.nextButt = (1007, 660)  # coord of Next button on scheduler pop up window just above
            self.schedIcon = (1056, 337)  # largish Schedules icon on top right of screen
            self.filterIcon = (227, 223)  # coord of small Filter icon top left for colour check
            self.filterButt = (246, 223)  # coord of filter button
            self.filterInputBar = (376, 261)  # coord of bar for choosing which positions to filter out for viewing on schedule
            self.LA = (410, 310)  # vals for work com: (478, 309) # Coords for LA role in drop down filter menu
            self.applyButt = (1629, 301)  # coords of Apply button on filter menu
            self.monthlyCal = (1087, 188)  # coords for opening monthly calendar for choosing day to view on screen





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
            time.sleep(0.5)  # used to add gap between text input and pressing enter
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
        self.moveMouse(22, 462, 0.5, 'y')  # click eraser selection button

    def otf(self):
        '''
        select the otf activity function from side pane
        inputs: none
        '''
        self.moveMouse(24, 427, 0.5, 'y')  # open activity pane
        self.moveMouse(66, 813, 0.5, 'y')  # select otf from list

    def logProgress(self, action, value):
        '''
        Logs the status of certain steps in the automation process such as finding elements on the screen
        Inputs: Action: string of the name of the action to log, eg element colour
        Value: str (or int) of key. Eg, True, complete
        '''
        action = str(action)
        self.progressDict[action] = value
        print(self.progressDict.items())

    def get(self,value):
        '''
        A master getter method. Input an argument to specify which values you want.
        Returns: tuple(x cor, y cor)
        input: value (str): ex: 'logo'
        return: tuple (x coord,ycoord) for the coords needed for the given parameter. Ex. 'logo' return position of the logo on screen
        '''

        if value == 'logo':
            return self.logo # coordinates of huge "D" on main screen
        if value == 'loginButt':
            return self.loginButt  # coord. of main Login button on main screen
        if value == 'schedRadButt':
            return self.schedRadButt # coord of Scheduler radio button on first pop up before entering main program
        if value == 'nextButt':
            return self.nextButt  # coord of Next button on scheduler pop up window just above
        if value == 'schedIcon':
            return self.schedIcon  # largish Schedules icon on top right of screen
        if value == 'filterIcon':
            return self.filterIcon # coord of small Filter icon top left for colour check
        if value == 'filterButt':
            return self.filterButt # coord of filter button
        if value == 'filterInputBar':
            return self.filterInputBar # coord of bar for choosing which positions to filter out for viewing on schedule
        if value == 'LA':
            return self.LA # vals for work com: (478, 309) # Coords for LA role in drop down filter menu
        if value == 'applyButt':
            return self.applyButt   # coords of Apply button on filter menu
        if value == 'monthlyCal':
            return self.monthlyCal   # coords for opening monthly calendar for choosing day to view on screen


    def clickDate(self):

        '''
        This function gets the current date and then calculates the position of that date on the calendar and clicks it.
        It contains a helper function called week() which gathers the week number a certain date is in, ex week 1, week 2
        '''

        def weekdayConver(curDate):
            '''
            Convert the normal return values of .weekday() to the needed values for this program where Sunday must be 0,
            Monday 1...
            :param curDate: Obj of the current date or any date you choose to input
            :return: int for each day of the week with Sun as 0
            '''

            day = curDate.weekday()  # extract the weekday int from the datetime object

            if day == 6: # Sunday
                return 0 # convert to 0 as Sunday
            if day == 5: # Sat
                return 6
            if day == 4: # Fri
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
        # print(day)
        # print(week())
        yDiff = 32  # number of pixels between adjacent rows (eg week 1 - week 2) (work 32, home 37)
        xDiff = 36  # number of pixels between immediately adjacent days of week (eg:mon-tues) (work 36, home 44)
        xDefault = 851  # 36 pixel difference (work 851, home com 857)
        yDefault = 301  # (work 301, home com 381) (x=857, y=378)

        x = xDefault + (day * xDiff)

        if week() == 1:
            y = yDefault  # if needed the first week of the month supply only the yDefault
        else:  # if needing other weeks, subtract 1 and mulitply by the yDiff (pixel difference) week 2 = (2-1)*yDiff
            y = yDefault + ((week() - 1) * yDiff)
        print(x, y)
        self.moveMouse(x, y, 0.5, 'y')

ts1=TaskSet('w')

ts1.moveMouse(173, 68, 0.2, 'y')  # click on blank area of browser to focus the browser
path="C:/Users/aswitzer/Downloads/" # this does not work. the default location is the scratches folder

for num in range(1, 8): # cycle through days of the week from sun to sat
    ts1.pressKeys('ctrl', str(num))
    screenshot = ImageGrab.grab()  # Take the screenshot
    screenshot.save(path+str(num)+".png", 'PNG') # saves to the scratches folder as default if only a file name is given image.png
    print(str(num),'completed')
    time.sleep(1)

time.sleep(1)
screenshot.save(path+str(8)+".png", 'PNG')
