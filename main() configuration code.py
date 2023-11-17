# Contents #

# 1. calls for a full setup of desktop
# 2. calls for a single instance of DF 



#### 1. Below is the main list of calls for running a full setup for scheduling ####

def main():

    print('\nEnsure bookmarks bar is on')

    taskSet1=TaskSet() # Scheduling for LA and Pages
    taskSet2=TaskSet() # Sharepoint calendar
    taskSet3=TaskSet() # Calendar for week of scheduling
    taskSet4=TaskSet() # Dayforce for current day
    taskSet5=TaskSet() # Open Email

    taskSet1.moveMouse(605, 1056, 0.5, 'y')  # go to Firefox (5 position on taskbar)
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
    if taskSet4.confirmElement('Schedules.png', 'n', 1007, 370, 1113, 397):
        taskSet1.moveMouse(1056, 337, 0.5, 'y')  # click schedule (main button to load sched)
    if taskSet1.confirmElementCol(227, 223, (28, 68, 156)):  # Check for filter button by colour of icon
        taskSet1.moveMouse(246, 223, 0.2, 'y')  # click Filter button
    taskSet1.moveMouse(376,261,0.5,'y') # click filter input bar
    taskSet1.moveMouse(410,310,0.2,'y') # select LA
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
    if taskSet4.confirmElement('Schedules.png', 'n', 1007, 370, 1113, 397):
        taskSet1.moveMouse(1056, 337, 0.5, 'y')  # click schedule (main button to load sched)
    if taskSet1.confirmElementCol(227, 223, (28, 68, 156)):  # Check for filter button by colour of icon
        taskSet1.moveMouse(246, 223, 0.2, 'y')  # click Filter button
    taskSet1.moveMouse(376, 261, 0.5, 'y')  # click filter input bar
    taskSet1.moveMouse(396, 390, 0.2, 'y')  # select Page
    taskSet1.moveMouse(1629, 301, 0.2, 'y')  # click Apply button
    taskSet1.moveMouse(1087, 188, 0.5, 'y')  # open calendar

    # Open Sharepoint
    taskSet2.pressKeys('ctrl', 't')  # open new tab
    taskSet2.moveMouse(53, 97, 1, 'y')  # click Sharepoint (on bookmarks tab)
    if taskSet2.confirmElementCol(215, 133, (56, 00, 00)):
        taskSet2.moveMouse(21, 134, 0.5, 'y')  # click Sharepoint menu button (left side)
    if taskSet2.confirmElement('Calendar.png', 'n', 25, 428, 65, 467):
        taskSet2.moveMouse(88, 447, 0.5, 'y')  # open calendar
    taskSet2.moveMouse(702,20,1,'y')

    # Open Sharepoint
    taskSet3.pressKeys('ctrl', 't')  # open new tab
    taskSet3.moveMouse(53, 97, 1, 'y')  # click Sharepoint
    if taskSet3.confirmElementCol(215, 133, (56, 00, 00)):
        taskSet3.moveMouse(21, 134, 0.5, 'y')  # click Sharepoint menu button (left side)
    if taskSet3.confirmElement('Calendar.png', 'n', 25, 428, 65, 467):
        taskSet3.moveMouse(88, 447, 0.5, 'y')  # open calendar
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
    if taskSet4.confirmElement('Schedules.png', 'n', 1007, 370, 1113, 397):
        taskSet1.moveMouse(1056, 337, 0.5, 'y')  # click schedule (main button to load sched)
    if taskSet4.confirmElementCol(227, 223, (28, 68, 156)):  # Check for filter button by colour of icon
        taskSet4.moveMouse(246, 223, 0.2, 'y')  # click Filter button
    taskSet4.moveMouse(376, 261, 0.5, 'y')  # click filter input bar
    taskSet4.moveMouse(410, 310, 0.5, 'y')  # select LA
    taskSet4.moveMouse(1629, 301, 0.2, 'y')  # click Apply button
    taskSet4.moveMouse(1087, 188, 0.5, 'y')  # open calendar

    # Open Email
    taskSet5.pressKeys('ctrl', 't')  # open new tab
    taskSet5.moveMouse(53, 97, 1, 'y')  # click Sharepoint (on bookmarks tab)
    if taskSet5.confirmElementCol(215, 133, (56, 00, 00)):
        taskSet5.moveMouse(21, 134, 0.5, 'y')  # click Sharepoint menu button (left side)
    if taskSet5.confirmElement('Calendar.png', 'n', 25, 428, 65, 467):
        taskSet5.moveMouse(83, 254, 0.5, 'y')  # open email (Outlook)



main()


#### 2. Below is the config code for running DfQuickCheck.py; this opens one instance of schedule

 taskSet4=TaskSet()


    taskSet4.moveMouse(173, 68, 0.5, 'y')  # click on blank area of browser to focus the browser
    taskSet4.pressKeys('ctrl', 't')  # open new tab (try to add delay here)
    taskSet4.type('dayforcehcm.com', 'y')  # Go to site
    # if taskSet4.confirmElement('Company.png','cr') == True: # monitor for when Select Role box displays then select Daily Scheduler (tiny radio button)
    if taskSet4.confirmElementCol(665,575, (48,103,219)):
        taskSet4.moveMouse(1226, 640, 0.25, 'y')  # go to autofill user name; Firefox should auto pop this up
    taskSet4.moveMouse(1226, 737, 0.2, 'y')  # go to Login
    if taskSet4.confirmElement('SelectRole.png','c'): # monitor for when Select Role box displays then select Daily Scheduler (tiny radio button)
        taskSet4.moveMouse(915, 548, 0.5,'y')  # select Daily Scheduler (small box before sched loaded) !if this is missed the next function will not be available (shedule button)
    taskSet4.moveMouse(1007, 660, 0.2, 'y')  # click next (on small box)
    if taskSet4.confirmElement('Schedules.png','n',1007,370,1113,397):
        taskSet4.moveMouse(1056, 337, 0.5, 'y')  # click schedule (main button to load sched)
    if taskSet4.confirmElementCol(227, 223, (28, 68, 156)): # Check for filter button by colour of icon
        taskSet4.moveMouse(246, 223, 0.2, 'y')  # click Filter button
    taskSet4.moveMouse(376, 261, 0.5, 'y')  # click filter input bar
    taskSet4.moveMouse(410, 310, 0.5, 'y')  # select LA
    taskSet4.moveMouse(1629, 301, 0.2, 'y')  # click Apply button
    taskSet4.moveMouse(1087, 188, 0.5, 'y')  # open calendar
