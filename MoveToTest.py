# Simple function for testing where the mouse will go with certain coordinates
import pyautogui as ag





def moveMouse(x,y,duration=1):
    ag.moveTo(x,y,1)


moveMouse()
