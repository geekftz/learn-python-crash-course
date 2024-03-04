from random import randint

class Die():
    """a class to represent die"""
    def __init__(self, num_sides=6):
        """die default to 6 sides"""
        self.num_sides = num_sides

    def roll(self):
        """return a random value between 1 and sides number of die"""
        return randint(1, self.num_sides)