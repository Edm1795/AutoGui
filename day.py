import pyautogui as ag
import datetime


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
