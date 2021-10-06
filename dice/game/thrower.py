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

<<<<<<< HEAD
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
=======
    def __init__(self):
        """
        
        Attributes:
            dice (list): Hold the dice value for each throw
            num_throws (number): Keeps track of the number of throws in the game
        """

        self.dice = []
        self.num_throws = 0


    def get_points(self):
        """
        get_points evaluates the throw then calculates the score and return it to the total

        "1" are worth 100 points
        "5" are worht 50 points
        
        """
        
        score = 0

        for i in self.dice:
            if i == 1:
                score += 100
            if i == 5:
                score += 50
            
        return score




    def throw_dice(self):
        """
        throw_dice method controls and records the throw of the dice
        
        """
        
        self.dice.clear() # clears last throw
        for i in range(5):# for loop to get 5 numbers between 1-5
            die = random.randint(1, 6)
            self.dice.append(die) #append die to dice list

        self.num_throws +=1 # add one to the num_throws counter

    

    def can_throw(self):
        """
        can_throw method checks if the thrower gets another turn if the previous
                    throw had a 5 or a 1 or if the num_throws is 0. 

        """

        for i in self.dice:
            if 5 in self.dice or 1 in self.dice or (self.num_throws == 0):
                return True
            else:
                return False
>>>>>>> 2663ed3d3721ad29c6ebd7d3df49cba088e6a506
