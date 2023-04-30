import random

class Dice:
    def __init__(self, diceCount : int) -> None:
        self.diceCount = diceCount
        self.mini = 1
        self.maxi = 6
        
    def rollDice(self):
        self.totalSum = 0
        self.diceUsed = 0
        
        # roll the dice till the number of diceCount using random.randint() 
        # and add it to totalSum
        while (self.diceUsed < self.diceCount):
            self.totalSum += random.randint(self.mini, self.maxi)
            self.diceUsed += 1
        
        return self.totalSum
