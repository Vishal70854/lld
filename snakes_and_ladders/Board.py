from typing import List
import random
from Jump import Jump
from Cell import Cell

class Board:
    def __init__(self, boardSize, numberOfSnakes, numberofLadders) -> None:
        self.boardSize = boardSize
        self.numberOfSnakes = numberOfSnakes
        self.numberofLadders = numberofLadders
        self.cells = [[Cell() for j in range(boardSize)] for i in range(boardSize)] # initialize cells 2-D array
        self.addSnakesAndLadders(self.cells, self.numberOfSnakes, self.numberofLadders)

    def getListCell(self) -> List[List[Cell]]:
        return self.cells       
    
    def addSnakesAndLadders(self, cells : List[List[Cell]], numberOfSnakes : int, numberofLadders : int) -> None:
        self.n = len(cells)
        # condition for snakes
        while numberOfSnakes > 0:
            self.snakeHead = random.randint(1, (self.n * self.n) - 1)  # between 1 - 100
            self.snakeTail = random.randint(1, (self.n * self.n) - 1)  # between 1 - 100
            if (self.snakeTail >= self.snakeHead):
                continue
            
            self.snakeObj = Jump()   # create Jump object
            self.snakeObj.start = self.snakeHead
            self.snakeObj.end = self.snakeTail
            
            self.cell = self.getCell(self.snakeHead)
            self.cell.jump = self.snakeObj
            # self.cellObj = self.getCell(self.snakeHead)
            # self.cell = self.cells[self.cellObj[0]][self.cellObj[1]]
            # self.cell.jump = self.snakeObj
            
            numberOfSnakes -= 1
        
        # condition for ladders
        while numberofLadders > 0:
            self.ladderStart = random.randint(1, (self.n * self.n) - 1)  # between 1 - 100
            self.ladderEnd = random.randint(1, (self.n * self.n) - 1)  # between 1 - 100
            
            if (self.ladderStart >= self.ladderEnd):
                continue
            
            self.ladderObj = Jump()   # create Jump object
            self.ladderObj.start = self.ladderStart
            self.ladderObj.end = self.ladderEnd

            self.cell = self.getCell(self.ladderStart)
            self.cell.jump = self.ladderObj
            # self.cellObj = self.getCell(self.ladderStart)
            # self.cell = self.cells[self.cellObj[0]][self.cellObj[1]]
            # self.cell.jump = self.ladderObj
            
            numberofLadders -= 1
    
    def getCell(self, start : int) -> Cell:
        row = start // 10
        col = start % 10
        # return (row, col)
        return self.cells[row][col]