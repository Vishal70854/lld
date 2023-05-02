# from Game import Game
# game = Game()
# game.startGame()

from Board import Board
b = Board(10, 5,  4)
cells = (b.getListCell())
b.addSnakesAndLadders(cells, 5 , 4)
print(b.getListCell())
b.initializeCells(10)