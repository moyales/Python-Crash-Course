from random import randint

class Die():
    """Models a standard die."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Prints a random number between 1 and n sides."""
        n = randint(1, self.sides)
        print("The", str(self.sides) + "-sided die rolled a", n)

standard = Die()
standard.roll_die()

ten = Die(10)
ten.roll_die()

twenty = Die(20)
twenty.roll_die()
