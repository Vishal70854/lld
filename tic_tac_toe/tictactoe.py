from board import Board
from collections import deque
from player import Player
from playingPieceX import PlayingPieceX
from playingPieceO import PlayingPieceO

class TicTacToe:
    def __init__(self):
        self.players = deque()
        self.gameBoard = Board(3)
        
    def initializeGame(self):
        crossPiece = PlayingPieceX()
        player1 = Player("Player1", crossPiece)
        
        naughtPiece = PlayingPieceO()
        player2 = Player("Player2", naughtPiece)
        
        self.players.append(player1)
        self.players.append(player2)

        # initialize game board
        # self.gameBoard = 
        
    def startGame(self):
        noWinner = True
        
        while noWinner:
            playerTurn = self.players.popleft() # remove the player from front of queue
            # print game board
            self.gameBoard.printBoard()
            # find free spaces
            freespaces = self.gameBoard.getFreeCells()
            if len(freespaces) == 0:
                noWinner = False
                continue
            
            print(f"PlayerTurn: {playerTurn.name}",end = " ")
            row, column = map(int,input("Enter row and column in comma separated:").split(","))
            # place the playingpiece in the board
            pieceAddedSuccessfully = self.gameBoard.addPiece(row, column, playerTurn.playingpiece)
            
            if not pieceAddedSuccessfully:
                print("Incorrect position. Please Try Again!")
                self.players.appendleft(playerTurn)
                continue
            self.players.append(playerTurn)
            
            winner = self.isThereWinner(row, column, playerTurn.playingpiece.piecetype) 
            if winner:
                return playerTurn.name
        
        return "It's a Tie!"
    
    def isThereWinner(self, row, column, piecetype):
        rowMatch = columnMatch = diagonalMatch = antidiagonalMatch = True
        n = len(self.gameBoard.board)
        # row check for winner
        for i in range(n):
            if (self.gameBoard.board[row][i] == None or 
                self.gameBoard.board[row][i].piecetype != piecetype):
                    rowMatch = False
        
        # column check for winner
        for i in range(n):
            if (self.gameBoard.board[i][column] == None or 
                self.gameBoard.board[i][column].piecetype != piecetype):
                    columnMatch = False
        
        # diagonal check for winner
        for i in range(n):
            if (self.gameBoard.board[i][i] == None or 
                self.gameBoard.board[i][i].piecetype != piecetype):
                    diagonalMatch = False
                
        # antidiagonal check for winner
        j = n - 1
        for i in range(n):
            if (self.gameBoard.board[i][j] == None or 
                self.gameBoard.board[i][j].piecetype != piecetype):
                    antidiagonalMatch = False
            j -= 1
        return rowMatch or columnMatch or diagonalMatch or antidiagonalMatch
   
            