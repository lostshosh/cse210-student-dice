import random

# TODO: Define the Thrower class here.
class Thrower:
    """
    Thower has the responsibility of the current throw of the dice, whether or not to throw again, 
    get the score of the dice.

    Attributes:
        can_throw (boolean): Whether or not the player can throw the dice.
        get_points (number): Scoreing the throw of the dice .
        throw_dice (number): Get a new throw of the dice.
    
    """

    dice = []
    num_throws = 0

    def __init__(self):




        self.can_throw = True
        self.get_points()
        self.throw_dice()



    def get_points(self):
        pass


    def throw_dice(self):
        pass

    

    def num_throws(self):
        pass