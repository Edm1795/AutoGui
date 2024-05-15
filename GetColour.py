import pyautogui as ag
from PIL import ImageGrab
import time

looping=True
while looping:

    # Get the screenshot of the screen
    screenshot = ImageGrab.grab()

    mousePos=ag.position()

    pixelColour = screenshot.getpixel(mousePos)
    print("Color value at coordinates",mousePos[0],mousePos[1], pixelColour)

    time.sleep(2)






#time.sleep(1.5)
## Get the screenshot of the screen
#screenshot = ImageGrab.grab()

## Get the color value of the pixel at coordinates (100, 200)
#x=353
#y=286
#ag.moveTo(x,y)
#pixel_color = screenshot.getpixel((x,y))
#print("Color value at coordinates",x,y, pixel_color)
