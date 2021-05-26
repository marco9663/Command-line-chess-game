from termcolor import colored
from Coordinate import Coordinate as C
from Move import Move
from Knight import Knight
from Queen import Queen
from Bishop import Bishop
from Rook import Rook

White = True
Black = False


# coord = Coordinate (e.g. tuple(row, col))
# side = color of the piece (e.g. WHITE or Black)
# board = current chess board (board Class)


class Pawn:
    value = 10
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
        self.symbol = "p"

    def __str__(self):
        return colored("p", "red" if self.side else "cyan")

    def getMoves(self):
        currentCoordinate = self.coord

        # forward one step
        advanceOnePosition = currentCoordinate + C(self.direction, 0)
        # If the move is not out of boundary
        if self.board.isValidPos(advanceOnePosition):
            row = advanceOnePosition[0]
            # if advance position is empty
            if self.board.pieceAtPosition(advanceOnePosition) is None:
                # if Pawn is an Top or Bottom row
                if row == 0 or row == 7:
                    # do something to promote
                    piecesForPromotion = [Rook(self.board, self.side, advanceOnePosition),
                                          Knight(self.board, self.side, advanceOnePosition),
                                          Bishop(self.board, self.side, advanceOnePosition),
                                          Queen(self.board, self.side, advanceOnePosition)]
                    for piece in piecesForPromotion:
                        move = Move(self, advanceOnePosition)
                        move.promotion = True
                        move.specialMovePiece = piece
                        yield move
                else:
                    yield Move(self, advanceOnePosition)

        # forward two step
        if self.movesMade == 0:
            advanceTwoPosition = currentCoordinate + C(self.direction * 2, 0)
            # if advance position and the path to it is empty
            if self.board.pieceAtPosition(advanceOnePosition) is None and \
                    self.board.pieceAtPosition(advanceTwoPosition) is None:
                yield Move(self, advanceTwoPosition)

        # Pawn take
        movements = [C(self.direction, 1), C(self.direction, -1)]
        for movement in movements:
            newPosition = self.coord + movement
            # if the new position is inbound
            if self.board.isValidPos(newPosition):
                pieceToTake = self.board.pieceAtPosition(newPosition)
                # if there is a piece to take and belongs to opponent
                if pieceToTake and pieceToTake.side != self.side:
                    row = newPosition[0]
                    if row == 0 or row == 7:
                        piecesForPromotion = [Rook(self.board, self.side, newPosition),
                                              Knight(self.board, self.side, newPosition),
                                              Bishop(self.board, self.side, newPosition),
                                              Queen(self.board, self.side, newPosition)]
                        for piece in piecesForPromotion:
                            move = Move(self, newPosition, capturing=pieceToTake)
                            move.promotion = True
                            move.specialMovePiece = piece
                            yield move
                    else:
                        yield Move(self, newPosition, capturing=pieceToTake)

        # En passant
        movements = [C(self.direction, 1), C(self.direction, -1)]
        for movement in movements:
            # column number +1 / -1 positon of the pawn
            posBesidePawn = self.coord + C(0, movement[1])
            # if the pos is in board
            if self.board.isValidPos(posBesidePawn):
                # get the piece beside pawn
                pieceBesidePawn = self.board.pieceAtPosition(posBesidePawn)
                # get the last moved piece
                lastPieceMoved = self.board.getLastPieceMoved()
                # init
                lastMoveWasAdvanceTwo = False
                lastMove = self.board.getLastMove()

                # check if there is last move
                if lastMove:
                    # check if the last move is two step forward
                    if lastMove.newPosition - lastMove.oldPosition == C(2, 0) or \
                            lastMove.newPosition - lastMove.oldPosition == C(-2, 0):
                        lastMoveWasAdvanceTwo = True

                # check if there is piece beside pawn & pawn beside pawn & not our side &
                if pieceBesidePawn and \
                        pieceBesidePawn.symbol == 'p' and \
                        pieceBesidePawn.side != self.side and \
                        lastPieceMoved is pieceBesidePawn and \
                        lastMoveWasAdvanceTwo:
                    move = Move(self, self.coord + movement, capturing=pieceBesidePawn)
                    move.passant = True
                    move.specialMovePiece = pieceBesidePawn
                    yield move
