from random import randint

class Dice():

    def __init__(self, side=6):

        self.side = side

    def rolling(self):

        side = randint(1,6)
        print(side)

class TenDice(Dice):

    def __init__(self, side=6):
        super().__init__(side)

    def rolling(self):

        side = randint(1,10)
        print(side)

ten_rolls = TenDice()

for rolls in range(10):
    ten_rolls.rolling()
    
