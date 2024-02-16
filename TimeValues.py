class TimeValues:
    '''
    A class which holds a variety of time values to use for moving the mouse accross the screen.
    This standardizes the timings for automation and allows for easy alteration of timings across
    the whole program. Upon instantiation you can choose a speed range such as 'f' for fast where all
    values are set to shorter (and thus faster) timings.
    Inputs: str: 'f' gives all fastest values; 'm' gives medium values; 's' gives slow values
    '''

    def __init__(self, speed):
        if speed == 'f':
            self.fast = 0.1
            self.med = 0.2
            self.slow = 0.3
        if speed == 'm':
            self.fast = 0.2
            self.med = 0.4
            self.slow = 0.5
         if speed == 's':
            self.fast = 0.4
            self.med = 0.5
            self.slow = 0.8

    def getFast(self):
        return self.fast

    def getMed(self):
        return self.med

    def getSlow(self):
        return self.slow
