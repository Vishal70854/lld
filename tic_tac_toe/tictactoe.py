from board import Board
from collections import deque
from player import Player
from pieceType import PieceType
from playingPieceX import PlayingPieceX
from playingPieceO import PlayingPieceO

class TicTacToeGame:
    def __init__(self):
        self.players = deque()
        self.game_board = None

    def initialize_game(self) -> None:
        cross_piece = PlayingPieceX()
        player1 = Player('Player1', cross_piece)

        noughts_piece = PlayingPieceO()
        player2 = Player('Player2', noughts_piece)

        self.players.append(player1)
        self.players.append(player2)

        self.game_board = Board(3)

    def start_game(self) -> str:
        no_winner = True
        while no_winner:
            player_turn = self.players.popleft()

            free_spaces = self.game_board.get_free_cells()
            if not free_spaces:
                no_winner = False
                continue

            print(f'Player {player_turn.name} turn:')
            self.game_board.print_board()

            while True:
                try:
                    input_row, input_col = map(int, input('Enter row,column: ').split(','))
                    break
                except ValueError:
                    print('Invalid input. Please enter two integers separated by a comma.')

            piece_added_successfully = self.game_board.add_piece(input_row, input_col, player_turn.playing_piece)
            if not piece_added_successfully:
                self.players.appendleft(player_turn)
                print('That space is already taken. Please try again.')
                continue

            if self.check_for_winner():
                return f'{player_turn.name} wins!'
            
            if not self.players:
                no_winner = False
                continue
            
            self.players.append(player_turn)

    def check_for_winner(self) -> bool:
        board_size = len(self.game_board.board)
        
        # Check rows and columns for a win.
        for i in range(board_size):
            if all(cell == 'X' for cell in self.game_board.board[i]):
                return True
            elif all(cell == 'O' for cell in self.game_board.board[i]):
                return True
            
            if all(row[i] == 'X' for row in self.game_board.board):
                return True
            elif all(row[i] == 'O' for row in self.game_board.board):
                return True
        
        # Check diagonals for a win.
        if all(self.game_board.board[i][i] == 'X' for i in range(board_size)):
            return True
        elif all(self.game_board.board[i][i] == 'O' for i in range(board_size)):
            return True
        
        if all(self.game_board.board[i][board_size - 1 - i] == 'X' for i in range(board_size)):
            return True
        elif all(self.game_board.board[i][board_size - 1 - i] == 'O' for i in range(board_size)):
            return True
        
        return False
    
