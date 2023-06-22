from playingPieceType import PlayingPieceType
from playingPiece import PlayingPiece

class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PlayingPieceType.X.name)
        
