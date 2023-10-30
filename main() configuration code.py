 print('\nEnsure bookmarks bar is on')

    taskSet1=TaskSet() # Scheduling for LA and Pages
    taskSet2=TaskSet() # Sharepoint calendar
    taskSet3=TaskSet() # Calendar for week of scheduling
    taskSet4=TaskSet() # Dayforce for current day
    taskSet5=TaskSet() # Open Email

    taskSet1.moveMouse(605, 1056, 1, 'y')  # go to Firefox
    time.sleep(2) # delay for first case scenerio; more time needed to open Firefox
    # taskSet1.pressKeys('ctrl', 't')  # open new tab (try to add delay here)
    taskSet1.type('dayforcehcm.com', 'y')  # Go to site (consider adding click to addre. bar to ensure cursor)
    taskSet1.moveMouse(1226, 640, 3, 'y')  # go to autofill user name; Firefox should auto pop this up
    taskSet1.moveMouse(1226, 737, 0.2, 'y')  # go to Login
    taskSet1.moveMouse(915, 548, 7, 'y')  # select Daily Scheduler (small box before sched loaded) !if this is missed the next function will not be available (shedule button)
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
    taskSet1.moveMouse(1226, 640, 3, 'y')  # go to autofill user name; Firefox should auto pop this up
    taskSet1.moveMouse(1226, 737, 0.2, 'y')  # go to Login
    taskSet1.moveMouse(915, 548, 7, 'y')  # select Daily Scheduler (small box before sched loaded)
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
    taskSet2.moveMouse(21, 134, 5, 'y')  # click Sharepoint menu button (left side)
    taskSet2.moveMouse(88, 447, 2, 'y')  # open calendar
    taskSet2.moveMouse(702,20,1,'y')

    # Open Sharepoint
    taskSet3.pressKeys('ctrl', 't')  # open new tab
    taskSet3.moveMouse(53, 97, 1, 'y')  # click Sharepoint
    taskSet3.moveMouse(21, 134, 1, 'y')  # click outlook menu button (left side)
    taskSet3.moveMouse(88, 447, 2, 'y')  # open calendar
    taskSet3.moveMouse(572, 269, 1, 'y')  # open date selection calendar
    taskSet3.moveMouse(926, 22, 1, 'y')  # open calendar

    taskSet3.moveMouse(828, 22, 1, 'y')  # open calendar
    taskSet3.drag(-1107,18,1,'l') # drag calendar to left screen

    # Open last instance of Dayforce for current day
    taskSet4.moveMouse(173, 68, 1, 'y')  # click on blank area of browser to focus the browser
    taskSet4.pressKeys('ctrl', 't')  # open new tab (try to add delay here)
    taskSet4.type('dayforcehcm.com', 'y')  # Go to site
    taskSet4.moveMouse(1226, 640, 3, 'y')  # go to autofill user name; Firefox should auto pop this up
    taskSet4.moveMouse(1226, 737, 0.2, 'y')  # go to Login
    taskSet4.moveMouse(915, 548, 7, 'y')  # select Daily Scheduler (small box before sched loaded)
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
    taskSet5.moveMouse(21, 134, 5, 'y')  # click Sharepoint menu button (left side)
    taskSet5.moveMouse(83, 254, 2, 'y')  # open email (Outlook)
