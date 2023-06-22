from playingPiece import PlayingPiece

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]
        
    def addPiece(self, row : int, col : int, playingpiece : PlayingPiece) -> bool:
        if self.board[row][col] != None:
            return False
        self.board[row][col] = playingpiece
        return True
    
    def getFreeCells(self):
        freecells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == None:
                    freecells.append([i,j])
        return freecells

    def printBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != None:
                    print("check", self.board[i][j])
                    print(self.board[i][j].piecetype.name)
                else:
                    print("    ", end = "")
                print(" | ",end = "")
            print("\n")