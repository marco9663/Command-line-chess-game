from termcolor import colored
from Coordinate import Coordinate as C
from Move import Move

White = True
Black = False


class Knight:
    value = 30

    def __init__(self, board, side, coord, movesMade=0):
        if side:
            self.side = White
            self.direction = -1
        else:
            self.side = Black
            self.direction = 1
        self.board = board
        self.coord = coord
        self.movesMade = movesMade
        self.symbol = "n"
    def __str__(self):
        return colored("n", "red" if self.side else "cyan")

    def getMoves(self):
        currentCoordinate = self.coord
        # possible move
        movements = [C(2, 1), C(2, -1), C(-2, 1), C(-2, -1),
                     C(1, 2), C(1, -2), C(-1, 2), C(-1, -2)]

        for movement in movements:
            newPosition = currentCoordinate + movement
            if self.board.isValidPos(newPosition):
                pieceAtNewPos = self.board.pieceAtPosition(newPosition)
                # check if new position is occupied
                if pieceAtNewPos is None:
                    yield Move(self, newPosition)
                elif pieceAtNewPos.side != self.side:
                    yield Move(self, newPosition, capturing=pieceAtNewPos)