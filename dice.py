from random import randint #use randint from random

class die:

# class constructor
    def __init__(self, sides):
      self.sides = sides

# allows for the update of the number of sides for a die
    def update_sides(self, sides):
      self.sides = sides

# return a random number from 1 to the number of sides the die has
    def roll(self):
      return randint(1, self.sides)

def rolling_the_dice(dice_sides): 
    
    # dice = []
    
    # for n in dice_sides:
      
    #   dice.append( die(n).roll() )
    
    # return dice

  return [die(x).roll() for x in dice_sides]


print( rolling_the_dice([12, 6, 24]) )