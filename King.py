from termcolor import colored
from Coordinate import Coordinate as C
from Move import Move

White = True
Black = False


class King:
    value = 900
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
        self.symbol = "k"

    def __str__(self):
        return colored("k", "red" if self.side else "cyan")

    def getMoves(self):
        currentCoordinate = self.coord

        movements = [C(0, 1), C(0, -1), C(1, 0), C(-1, 0),
                      C(1, 1), C(-1, 1), C(1, -1), C(-1, -1)]

        for movement in movements:
            newPosition = currentCoordinate + movement
            if self.board.isValidPos(newPosition):
                pieceAtNewPos = self.board.pieceAtPosition(newPosition)
                # check if new position is occupied
                if pieceAtNewPos is None:
                    yield Move(self, newPosition)
                elif pieceAtNewPos.side != self.side:
                    yield Move(self, newPosition, capturing=pieceAtNewPos)

        # Castling (only be done if the king has never moved)
        # the rook involved has never moved
        # the squares between the king and the rook involved are unoccupied
        # the king is not in check
        # the king does not cross over or end on a square attacked by an enemy piece
        if self.movesMade == 0:
            # The castling must be kingside or queenside.[5]
            # Neither the king nor the chosen rook has previously moved.
            # There are no pieces between the king and the chosen rook.
            # The king is not currently in check.
            # The king does not pass through a square that is attacked by an enemy piece.
            # The king does not end up in check. (True of any legal move.)
            inCheck = False
            kingsideCastleBlocked = False
            queensideCastleBlocked = False
            kingsideCastleCheck = False
            queensideCastleCheck = False
            kingsideRookMoved = True
            queensideRookMoved = True

            kingsideCastlePositions = [currentCoordinate + C(0, 1), currentCoordinate + C(0, 2)]
            # Check if any piece block the path in King's side
            for pos in kingsideCastlePositions:
                if self.board.pieceAtPosition(pos):
                    kingsideCastleBlocked = True
                    break

            queensideCastlePositions = [currentCoordinate + C(0, -1),
                                        currentCoordinate + C(0, -2),
                                        currentCoordinate + C(0, -3)]

            # Check if any piece block the path in Queen's side
            for pos in queensideCastlePositions:
                if self.board.pieceAtPosition(pos):
                    queensideCastleBlocked = True
                    break

            if kingsideCastleBlocked and queensideCastleBlocked:
                return

            # check if the path to new position and the old position is checked.
            otherSideMoves = self.board.getAllMoves(not self.side, includeKing=False)

            for move in otherSideMoves:
                if move.newPosition == self.coord:
                    inCheck = True
                    break
                if move.newPosition == self.coord + C(0, 1) or move.newPosition == self.coord + C(0, 2):
                    kingsideCastleCheck = True
                if move.newPosition == self.coord + C(0, -1) or move.newPosition == self.coord + C(0, -2):
                    queensideCastleCheck = True

            # check if king side rook is not moved
            kingsideRookPos = self.coord + C(0, 3)
            kingsideRook = self.board.pieceAtPosition(kingsideRookPos)
            if kingsideRook and kingsideRook.symbol == "r" and kingsideRook.movesMade == 0:
                kingsideRookMoved = False

            # check if queen side rook is not moved
            queensideRookPos = self.coord + C(0, -4)
            queensideRook = self.board.pieceAtPosition(queensideRookPos)
            if queensideRook and queensideRook.symbol == 'r' and queensideRook.movesMade == 0:
                queensideRookMoved = False

            if not inCheck:
                if not kingsideCastleBlocked and not kingsideCastleCheck and not kingsideRookMoved:
                    move = Move(self, currentCoordinate + C(0, 2))
                    rookMove = Move(kingsideRook, currentCoordinate + C(0, 1))
                    move.specialMovePiece = kingsideRook
                    move.kingsideCastle = True
                    move.rookMove = rookMove
                    yield move

                if not queensideCastleBlocked and not queensideCastleCheck and not queensideRookMoved:
                    move = Move(self, currentCoordinate + C(0, -2))
                    rookMove = Move(queensideRook, currentCoordinate + C(0, -1))
                    move.specialMovePiece = queensideRook
                    move.queensideCastle = True
                    move.rookMove = rookMove
                    yield move
