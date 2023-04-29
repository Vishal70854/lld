import random
from Jump import Jump
from Cell import Cell

class Board:
    def __init__(self, boardSize, numberOfSnakes, numberofLadders) -> None:
        self.boardSize = boardSize
        self.numberOfSnakes = numberOfSnakes
        self.numberofLadders = numberofLadders
        self.cells = [[None]*boardSize]*boardSize # initialize cells 2-D array
        self.initialize()
        
    def initialize(self):
        self.initializeCells(self.boardSize)    
        # self.addSnakesAndLadders(self.cells, self.numberOfSnakes, self.numberofLadders)
    
    def initializeCells(self, boardSize):
        for i in range(boardSize):
            for j in range(boardSize):
                
                self.cells[i][j] = Cell()   # create Cell object for each cells[i][j]
        return self.cells
    def addSnakesAndLadders(self, cells, numberOfSnakes, numberofLadders):
        # condition for snakes
        while numberOfSnakes > 0:
            self.snakeHead = random.randrange(1, len(cells) * len(cells) )  # between 1 - 100
            self.snakeTail = random.randrange(1, len(cells) * len(cells) )  # between 1 - 100
            
            if (self.snakeTail >= self.snakeHead):
                continue
            
            self.snakeObj = Jump()   # create Jump object
            self.snakeObj.start = self.snakeHead
            self.snakeObj.end = self.snakeTail

            self.cellObj = self.getCell(self.snakeHead)
            self.cell = self.cells[self.cellObj[0]][self.cellObj[1]]
            self.cell.jump = self.snakeObj
        numberOfSnakes -= 1
        
        # condition for ladders
        while numberofLadders > 0:
            self.ladderStart = random.randrange(1, len(cells) * len(cells) )  # between 1 - 100
            self.ladderEnd = random.randrange(1, len(cells) * len(cells) )  # between 1 - 100
            
            if (self.ladderStart >= self.ladderEnd):
                continue
            
            self.ladderObj = Jump()   # create Jump object
            self.ladderObj.start = self.ladderStart
            self.ladderObj.end = self.ladderEnd
            self.cellObj = self.getCell(self.ladderStart)
            self.cellObj.jump = self.ladderObj
        numberofLadders -= 1
    
    def getCell(self, start):
        self.row = start // self.boardSize
        self.col = start % self.boardSize
        return (self.row, self.col)
        # return self.cells[self.row][self.col]
    