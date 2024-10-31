# colour picker crtl shift a, Type in colour
import time

import DFQuickCheck
import TimeLine
from os.path import exists
from tkinter import *
from ScreenShot import *
from ctypes import windll  # used for fixing blurry fonts on win 10 and 11 (also  windll.shcore.SetProcessDpiAwareness(1))
import yaml



# Import pyscreeze 1.29 to pycharm, not directly into this module, otherwise another module related to pyscreeze (not sure how) will raise an exception if searching for the image on screen takes a little time



class MainWindow:

    def __init__(self, master,winPosHorVer,winSizeHorVert,mainFrameCol,lineColour,lineWidth,breadth,position,week,computer,pixelsPerMinute,eightAMline):

        # Master Window
        self.master = master
        self.master.title('AutoGui Ver. 1.4')
        self.master.geometry(winPosHorVer)  # position of the window in the screen (200x300) ("-3300+500")
        self.master.geometry(winSizeHorVert)  # set initial size of the root window (master) (1500x700);
        # self.master.iconbitmap("")
        self.master.iconphoto(False, PhotoImage(file="oneClick.png"))
        # if not set, the frames will fill the master window
        # self.master.attributes('-fullscreen', True)
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()

        self.master.attributes("-topmost", True)

        # Instantiate frames
        self.frame0 = Frame(self.master, bd=5, padx=5, bg='#606266')  # Top long row
        self.frame1 = Frame(self.master, bd=5, padx=5, bg='#2a2b2b')  # Side Column
        self.frame2 = Frame(self.master, bd=5, padx=5, bg=mainFrameCol)  # Main frame

        # Place frames
        self.frame0.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.frame1.grid(row=1, column=0, columnspan=1, sticky="nsew")
        self.frame2.grid(row=1, column=1, columnspan=1, sticky="nsew")

        # configure weighting of frames
        self.master.grid_columnconfigure(0,
                                         weight=1)  # First int refers to column numberAllows frames to expand as master window expands; weight tells how much of the columns it takes
        self.master.grid_columnconfigure(1, weight=7)  # weight gives 3 times as much column as the other columns
        # self.master.grid_columnconfigure(2, weight=1)
        self.master.grid_rowconfigure(1, weight=1)  # rowconfigure states: first row takes 1 parts of space

        self.frame1.grid_propagate(0)  # When adding widgets maintain weighting of frames
        self.frame2.grid_propagate(0)

        # sundries
        self.counter=0 # counter used for determining state of toggle switch used in transparency button

        frameWidth = 10  # Units are in characters not pixels

        windll.shcore.SetProcessDpiAwareness(1)  # used for fixing blurry fonts on win 10 and 11



        #  Entry widgets
        self.entry = Entry(self.frame0, width=10)
        self.entry.pack()

        #self.photo = PhotoImage(file="Speedometer2.png")
        #self.master.iconphoto(False, self.photo)


        self.button = Button(self.frame1, text="Schedule", width=12, command=lambda : self.schedule(lineColour,lineWidth))
        self.button.pack()

        self.button = Button(self.frame1, text="Screen Shot", width=12, command=lambda : self.screenShot(breadth,week,computer))
        self.button.pack()

        self.button = Button(self.frame1, text="Show Timeline", width=12, command=lambda : self.openTimeLine(lineColour,lineWidth,pixelsPerMinute,eightAMline))
        self.button.pack()

        self.button = Button(self.frame1, text="Close Timeline", width=12, command=self.closeTimeLine)
        self.button.pack()

        self.button = Button(self.frame1, text="Transparent", width=12, command=self.makeWinTrans)
        self.button.pack()

        self.positionLabel=Label(self.frame2,text='Position: ',bg='grey',)
        self.selected = StringVar() # selected is a fucntion with methods, use selected.get() to get the string val
        self.rad1 = Radiobutton(self.frame2, text='LAs', value='1',variable=self.selected) # ret 1 if desiring LAs
        self.rad2 = Radiobutton(self.frame2, text='Pages',value='2', variable=self.selected) # ret 2 if desiring Pages
        self.positionLabel.grid(row=0, column=0,sticky='w')
        self.rad1.grid(row=1,column=0,sticky='w')
        self.rad2.grid(row=2,column=0,sticky='w')


        # Labels

        # Display Screen shot information on screen, Computer, full week, position (eg:LA or p), week of month to be captured eg: first week of Feb)
        rawScreenShotText=formatScreenShotText(breadth,computer) # format the strings for use on the screen
        ScreenShotText=rawScreenShotText[0]+', '+rawScreenShotText[1]+', '+week # construct string displaying information about screenshot

        self.screenShotLabTitle = Label(self.frame2, text='Screen Shot:',font=(14),bg='grey')
        self.screenShotLabTitle.grid(row=3,column=0,sticky='w')
        self.screenShotLab = Label(self.frame2, text=ScreenShotText,font=(12))
        self.screenShotLab.grid(row=4,column=0,sticky='w')

        self.addItemButton = Button(self.frame1, text="Create New", width=12, command=self.createNew)
        self.addItemButton.pack()


    def schedule(self,lineColour,lineWidth):
        DFQuickCheck.main()
        TimeLine.main(lineColour,lineWidth,pixelsPerMinute,eightAMline)

    def setCount(self):
        self.counter+=1

    def closeTimeLine(self):
        try:
            TimeLine.close()
        except:
            pass

    def openTimeLine(self,lineColour,lineWidth,pixelsPerMinute,eightAMline):
        # Closes the currently showing timeline and re-runs timeline for the current time (the updated time)
        print(lineColour)
        try:
            TimeLine.close()
        except:
            TimeLine.main(lineColour,lineWidth,pixelsPerMinute,eightAMline)
        else:
            TimeLine.main(lineColour,lineWidth,pixelsPerMinute,eightAMline)

    def makeWinTrans(self):
        # this function turn the main window transparent and solid in alternation; it is a toggle function which uses
        # self.counter to know if the window needs to be opaque or solid
        if self.counter%2==0: # if pressing button to mke transparent
            opacIntList=[] # create empty list for holding opacity float values
            for num in range(4,10): # loop for filling list with needed opacity float values
                opacInt = num / 10 # eg: 4/10 = 0.4
                opacIntList.append(opacInt) # append to list [0.4,0.5,0.6...]
            # self.master.wm_attributes('-transparentcolor', '#2a2b2b')
            # self.master.wm_attributes('-transparentcolor', '#7E050C')
            for num in range(1,6): # loop for incrementally increasing opacity
                # pop values from list thus getting values from high to low
                self.master.attributes('-alpha', opacIntList.pop()) # attributes with alpha on the main window changes opacity of whole window
                time.sleep(0.1)
            self.setCount()
        else: # if pressing the same button to go back to regular solid colour
            self.master.attributes('-alpha', 1.0)
            self.setCount()
    def screenShot(self,breadth,week,computer):

        if mainWin.selected.get() == '1':
            screenShot=ScreenShot(breadth,'LA',week,computer)
            screenShot.takeShot()
        if mainWin.selected.get() == '2':
            screenShot = ScreenShot(breadth,'p',week,computer)
            screenShot.takeShot()


    def createNew(self):

        def click():
            pass

        text = Text(self.frame2, height=1)
        text.pack()

        text.insert('1.0', 'Set up click or text?')

        self.button = Button(self.frame2, text="Click", width=12, command=click)
        self.button.pack()

        self.addItemButton = Button(self.frame2, text="Text", width=12, command=self.createNew)
        self.addItemButton.pack()

def message(titleOfWin,message):
    """
    This function opens up a popup window, which displays a message
    inputs:
    titleOfWin: str
    message: str: the message you want to display
    """
    top = Toplevel()  # add bg="#373738" for colour.  Appears that the root (self.master) is not needed to run this window
    top.geometry("400x150")
    top.title(titleOfWin)

    # input for new item in stock
    messageLabel = Label(top, text=message, font=('Cambria 12'),wraplength=300)  # Label(top, text="Add New Item", font=('Mistral 18 bold')).place(x=150, y=80)
    messageLabel.pack()

def formatScreenShotText(breadth,computer):

    if computer == 'h':
        computer = 'Home'
    if computer == 'w':
        computer = 'Work'

    if breadth == 'f':
        breadth = 'Full'

    return(computer,breadth)


def main():
    global mainWin  # Global mainWin so as to access the mainWin from functions which may need to call method
    root = Tk()


    # Get configuration settings from external config yaml file

    if exists('config.yaml'):  # Returns True if file exists; if true open file and load into variable
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
            f.close()

            # set configuration values to variables
            winPosHorVer = config["winPosHorVert"]
            winSizeHorVert = config["winSizeHorVert"]
            mainFrameCol = config["mainFrameCol"]
            lineColour = config["timeLineCol"]
            lineWidth = config["timeLineWidth"]
            breadth = config["breadth"]
            position = config["position"]
            week = config["week"]
            computer = config["computer"]
            pixelsPerMinute = config["pixelsPerMinute"]
            eightAMline = config["eightAMline"]



    else:  # If no file exists initialize values to defaults
        print("### the config file was not found, default values have been loaded instead ###")
        winPosHorVer = "+1500+800"
        winSizeHorVert = "400x200"
        mainFrameCol = '#7E850C'
        lineColour="green"
        lineWidth="1"
        breadth = 'f'
        position = 'unknown'
        week = 'unknown'
        computer = 'w'   # Post message to screen if configuration file could not be found
        pixelsPerMinute = 1.0
        eightAMline = 500

        message('Message', 'The configuration file could not be found, and so the program is loaded with default settings.')

    mainWin = MainWindow(root,winPosHorVer,winSizeHorVert,mainFrameCol,lineColour,lineWidth,breadth,position,week,computer,pixelsPerMinute,eightAMline)

    root.mainloop()


main()

