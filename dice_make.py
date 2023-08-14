import random

class Dice:
    def __init__(self,a,b):
        self.min = a
        self.max = b

    def roll(self):
        return random.randint(self.min,self.max)