from playingPieceType import PlayingPieceType
from playingPiece import PlayingPiece

class PlayingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PlayingPieceType.O.name)
        