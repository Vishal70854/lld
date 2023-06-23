from pieceType import PieceType
from playingPiece import PlayingPiece
from typing import List

class Board:
    def __init__(self, size: int):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]

    def print_board(self) -> None:
        for row in self.board:
            print('|'.join(row))

    def get_free_cells(self) -> List[tuple]:
        free_cells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == ' ':
                    free_cells.append((i, j))
        return free_cells

    def add_piece(self, row: int, col: int, piece: PieceType) -> bool:
        if self.board[row][col] == ' ':
            self.board[row][col] = piece.name
            return True
        else:
            return False
