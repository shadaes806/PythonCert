from random import randint


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)


New = Dice(6)

print(New.roll_dice())


