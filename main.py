from random import randint #use randint from random

class die:

    def __init__(self, sides):
      self.sides = sides

    def update_sides(self, sides):
      self.sides = sides

    def roll(self):
      return randint(1, self.sides)

def rolling_the_dice(dice_sides): 
    
    # dice = []
    
    # for n in dice_sides:
      
    #   dice.append( die(n).roll() )
    
    # return dice

  return [die(x).roll() for x in dice_sides]



# randint

print( rolling_the_dice([12, 6, 24]) )