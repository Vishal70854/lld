from playingPiece import PlayingPiece

class Player:
    def __init__(self, name, playingpiece : PlayingPiece):
        self.name = name
        self.playingpiece = playingpiece
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
        
    def getPlayingPiece(self):
        return self.playingpiece

    def setPlayingPiece(self, playingpiece):
        self.playingpiece = playingpiece
        
        