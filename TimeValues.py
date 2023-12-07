class TimeValues:

    def __init__(self,speed):

        if speed=='f':
            self.fast=0.1
            self.med=0.2
            self.slow=0.3

    def getFast(self):

        return self.fast

    def getMed(self):

        return self.med
