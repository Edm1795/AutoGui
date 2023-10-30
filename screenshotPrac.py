import pyautogui as ag





im = ag.screenshot('Image.png') # takes screenshot and saves to same folder with title given in quotes

# ag.pixel((0, 0)) # Get colour value of pixel at given coordinates

# Returns True if a match
# ag.pixelMatchesColor(50, 200, (130, 135, 144)) # The first and second arguments are ints for x- and y-coord; the third arg is a tuple of three ints for the RGB color the screen pixel must match

b = ag.locateOnScreen('Image.png')

print(b)
