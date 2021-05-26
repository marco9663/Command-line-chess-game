from termcolor import colored
from Coordinate import Coordinate as C
from Move import Move

White = True
Black = False


class Queen:
    value = 90

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
        self.symbol = "q"

    def __str__(self):
        return colored("q", "red" if self.side else "cyan")

    def getMoves(self):
        currentCoordinate = self.coord
        directions = [C(0, 1), C(0, -1), C(1, 0), C(-1, 0),
                      C(1, 1), C(-1, 1), C(1, -1), C(-1, -1)]

        for direction in directions:
            for dis in range(1, 8):
                movement = C(dis * direction[0], dis * direction[1])
                newPosition = currentCoordinate + movement
                if self.board.isValidPos(newPosition):
                    pieceAtNewPos = self.board.pieceAtPosition(newPosition)
                    if pieceAtNewPos is None:
                        yield Move(self, newPosition)
                    else:  # if new position is not empty
                        # and belongs to the enemy
                        if pieceAtNewPos.side != self.side:
                            yield Move(self, newPosition, capturing=pieceAtNewPos)
                        # if block by same side then stop
                        break
