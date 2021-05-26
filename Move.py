from Input import coordinateToString, stringToCoordinate


class Move:
    def __init__(self, piece, toPosition, capturing=None):
        self.piece = piece
        self.oldPosition = piece.coord
        self.newPosition = toPosition
        self.capturing = capturing

        self.check = False
        self.checkmate = False
        self.kingsideCastle = False
        self.queensideCastle = False
        self.promotion = False
        self.passant = False
        self.stalemate = False
        self.specialMovePiece = None
        self.rookMove = None

    def __str__(self):
        cap = ""
        if self.capturing:
            cap = self.capturing.symbol
        else:
            cap = "none"

        return f"{self.piece.symbol}: {coordinateToString(self.oldPosition)} to " \
               f"{coordinateToString(self.newPosition)} (Capture: {cap})"

    def __eq__(self, other):
        if self.oldPosition == other.oldPosition and self.newPosition == other.newPosition:
            return True
        return False
