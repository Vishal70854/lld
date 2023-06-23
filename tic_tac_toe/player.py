from pieceType import PieceType
class Player:
    def __init__(self, name: str, playing_piece: PieceType):
        self.name = name
        self.playing_piece = playing_piece
