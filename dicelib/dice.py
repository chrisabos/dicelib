import random

class Dice():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        self.value = 0

    #rolls the dice
    def roll(self):
        self.value = random.randint(1, self.num_sides)

    #allows dice to be cast to int
    def __index__(self):
        return self.value

    #allows dice to be cast to int (older versions of python)
    def __int__(self):
        return self.value

    #allows dice to be cast as string
    def __str__(self):
        if(self.num_sides == 0):
            return self.__index__()
        return f'{self.num_sides} sided dice: {self.value}'

    #defines actions of adding two dice
    def __add__(self, other_dice):
        return self.value + other_dice.value

    #allows a list of dice to be an input to the "sum" python function
    def __radd__(self, other):
        if type(other) is int:
            return other + self.value
        return self.__add__(other)
