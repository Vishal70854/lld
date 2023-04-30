from collections import deque
from Board import Board
from Dice import Dice
from Player import Player

class Game:
    def __init__(self) -> None:
        self.board = Board(10, 5, 4)    # (boardSize, numberofsnakes, numberofladders)
        self.dice = Dice(1)
        self.playerList = deque()  # queue of Players
        self.winner = None
        self.addPlayers()
        
        #------------------------
        # player1 = Player("p1", 0)   #(playerid, currentPosition)
        # player2 = Player("p2", 0)   #(playerid, currentPosition)
        # self.playerList.append(player1)
        # self.playerList.append(player2)

        # self.cells = self.board.cells
        # print(self.cells)
        
        # self.initializeGame()
    
    # def initializeGame(self):
    #     self.board = Board(10, 5, 4)    # (boardSize, numberofsnakes, numberofladders)
    #     self.dice = Dice(1)
    #     self.playerList = deque()   # queue of Players
    #     self.winner = None
    #     self.addPlayers()

    def addPlayers(self):
        player1 = Player("p1", 0)   #(playerid, currentPosition)
        player2 = Player("p2", 0)   #(playerid, currentPosition)
        self.playerList.append(player1)
        self.playerList.append(player2)
        
    def findPlayerTurn(self) -> Player :
        self.currPlayer = self.playerList.popleft()
        self.playerList.append(self.currPlayer)
        return self.currPlayer
    
    def startGame(self) -> None:
        while self.winner == None:
            #check whose turn is now
            self.playerTurn = self.findPlayerTurn()
            print(f'Player turn is {self.playerTurn.id}, current position is {self.playerTurn.currentPosition}')
            
            # roll the dice
            self.diceNumbers = self.dice.rollDice()
            
            # get new position of dice
            self.playerNewPosition = self.playerTurn.currentPosition + self.diceNumbers
            if self.playerNewPosition >= (len(self.board.cells)**2 ):
                continue
            self.playerNewPosition = self.jumpCheck(self.playerNewPosition)
            self.playerTurn.currentPosition = self.playerNewPosition
            
            print(f'Player turn is {self.playerTurn.id}, new position is {self.playerTurn.currentPosition}')
            
            #check for winning condition
            if (self.playerNewPosition >= (len(self.board.cells) * len(self.board.cells) - 1)):
                self.winner = self.playerTurn
                
                print(f'Winner is {self.winner.id}')
                break

    def jumpCheck(self, playerNewPosition : int) -> int :
        
        '''
        self.cellObj = self.getCell(self.snakeHead)
        self.cell = self.cells[self.cellObj[0]][self.cells[self.cellObj[1]]]
        '''
        # self.cellObj = self.board.getCell(playerNewPosition)
        # self.cell = self.board.cells[self.cellObj[0]][self.cellObj[1]]
        self.cell = self.board.getCell(int(playerNewPosition))
        
        if self.cell.jump != None and self.cell.jump.start == playerNewPosition:
            if self.cell.jump.start <= self.cell.jump.end:
                print("jump done by : ladder")
            else:
                print("jump done by : snake")
            return self.cell.jump.end
        return playerNewPosition
    