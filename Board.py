from Pawn import Pawn
from Knight import Knight
from Queen import Queen
from Rook import Rook
from Bishop import Bishop
from King import King
from Coordinate import Coordinate as C

WHITE = True
BLACK = False
sqTable = {
    "p": ((0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
          (5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0),
          (1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0),
          (0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5),
          (0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0),
          (0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5),
          (0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5),
          (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)),
    "n": ((-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0),
          (-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0),
          (-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0),
          (-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0),
          (-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0),
          (-3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0),
          (-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0),
          (-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0)),
    "b": ((-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0),
          (-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0),
          (-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0),
          (-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0),
          (-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0),
          (-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0),
          (-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0),
          (-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0)),
    "r": ((0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
          (0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5),
          (-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5),
          (-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5),
          (-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5),
          (-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5),
          (-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5),
          (0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0)),
    "q": ((-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0),
          (-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0),
          (-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0),
          (-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5),
          (0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5),
          (-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0),
          (-1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0),
          (-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0)),
    "k": ((-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0),
          (-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0),
          (-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0),
          (-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0),
          (-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0),
          (-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0),
          (2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0),
          (2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0))
}


# White Side in Red color
# Black side in Cyan color


class Board:
    # Attribute for debugging
    # mateInOne - simulate check mate
    # passant - simulate En passant in board
    # promotion - simulate promotion in board
    def __init__(self, mateInOne=False, castleBoard=False, passant=False, promotion=False, stalemate=False):
        self.history = []
        # for showing White side advantage
        self.points = 0

        self.currentSide = WHITE
        self.movesMade = 0
        self.checkmate = False

        # init board with None
        self.board = [None] * 8
        for i in range(8):
            self.board[i] = [None] * 8

        if not mateInOne and not castleBoard and not passant and not promotion and not stalemate:
            # init Black side piece
            self.board[0][0] = Rook(self, BLACK, C(0, 0))
            self.board[0][1] = Knight(self, BLACK, C(0, 1))
            self.board[0][2] = Bishop(self, BLACK, C(0, 2))
            self.board[0][3] = Queen(self, BLACK, C(0, 3))
            self.board[0][4] = King(self, BLACK, C(0, 4))
            self.board[0][5] = Bishop(self, BLACK, C(0, 5))
            self.board[0][6] = Knight(self, BLACK, C(0, 6))
            self.board[0][7] = Rook(self, BLACK, C(0, 7))
            for i in range(8):
                self.board[1][i] = Pawn(self, BLACK, C(1, i))

            # init White side piece
            self.board[7][0] = Rook(self, WHITE, C(7, 0))
            self.board[7][1] = Knight(self, WHITE, C(7, 1))
            self.board[7][2] = Bishop(self, WHITE, C(7, 2))
            self.board[7][3] = Queen(self, WHITE, C(7, 3))
            self.board[7][4] = King(self, WHITE, C(7, 4))
            self.board[7][5] = Bishop(self, WHITE, C(7, 5))
            self.board[7][6] = Knight(self, WHITE, C(7, 6))
            self.board[7][7] = Rook(self, WHITE, C(7, 7))
            for i in range(8):
                self.board[6][i] = Pawn(self, WHITE, C(6, i))

        elif passant:
            self.board[1][1] = Pawn(self, BLACK, C(1, 1))
            self.board[1][0] = Pawn(self, WHITE, C(1, 0))
            self.board[0][1] = King(self, BLACK, C(0, 1))
            self.board[7][4] = King(self, WHITE, C(7, 4))

        elif mateInOne:
            self.board[1][3] = Rook(self, WHITE, C(1, 3))
            self.board[0][4] = King(self, BLACK, C(0, 4))
            self.board[7][4] = King(self, WHITE, C(7, 4))

        elif promotion:
            self.board[1][0] = Pawn(self, WHITE, C(1, 0))
            self.board[0][4] = King(self, BLACK, C(0, 4))
            self.board[7][4] = King(self, WHITE, C(7, 4))

        elif castleBoard:
            self.board[1][0] = Pawn(self, WHITE, C(1, 0))
            self.board[7][4] = King(self, WHITE, C(7, 4))
            self.board[0][4] = King(self, BLACK, C(0, 4))
            self.board[7][0] = Rook(self, WHITE, C(7, 0))
            self.board[7][7] = Rook(self, WHITE, C(7, 7))
            self.board[7][7].movesMade = 1

        elif stalemate:
            self.board[0][7] = King(self, BLACK, C(0, 7))
            self.board[1][5] = King(self, WHITE, C(1, 5))
            self.board[2][6] = Queen(self, WHITE, C(2, 6))

    def print_board(self):
        row = 8
        print(f"   a b c d e f g h\n")
        for i in range(8):
            print(row, end="  ")
            for j in range(8):
                piece = self.board[i][j] if self.board[i][j] else "x"
                print(piece, end=" ")
            print(f" {row}")
            row -= 1
        print(f"\n   a b c d e f g h\n")

    def mustPawnPromote(self, piece, newPos):
        if piece and piece.symbol == "p":
            if newPos[0] == 0 or newPos[0] == 7:
                return True
        return False

    def isCheckmate(self):
        # check no move can be made by the current side
        if len(self.getAllMoves(self.currentSide)) == 0:
            # check if checkmate by enemy
            for move in self.getAllMoves(not self.currentSide):
                pieceToTake = move.capturing
                if pieceToTake and pieceToTake.symbol == 'k':
                    return True
        return False

    def isStalemate(self):
        # check if no move can be made by the current side
        if len(self.getAllMoves(self.currentSide)) == 0:
            # check if checkmate by enemy
            for move in self.getAllMoves(not self.currentSide):
                pieceToTake = move.capturing
                if pieceToTake and pieceToTake.symbol == 'k':
                    return False
            # if no move and no check mate, then it is stalemate
            return True
        return False

    def isValidPos(self, pos):
        if 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7:
            return True
        else:
            return False

    def getPosPieceMove(self, pos):
        piece = self.pieceAtPosition(pos)
        if piece:
            moves = piece.getMoves()
            return moves

    def pieceAtPosition(self, Coord):
        return self.board[Coord[0]][Coord[1]]

    def getLastPieceMoved(self):
        if self.history:
            return self.history[-1].piece

    def getLastMove(self):
        if self.history:
            return self.history[-1]

    def getAllMoves(self, side, includeKing=True):
        allPieceMoves = []
        for row in self.board:
            for piece in row:
                # check if piece is empty and belong to the side
                if piece and piece.side == side:
                    if includeKing or piece.symbol != 'k':
                        for move in piece.getMoves():
                            allPieceMoves.append(move)
        return allPieceMoves

    def movePieceToPosition(self, piece, pos):
        oldRow = piece.coord[0]
        oldCol = piece.coord[1]
        newRow = pos[0]
        newCol = pos[1]
        self.board[oldRow][oldCol], self.board[newRow][newCol] = self.board[newRow][newCol], self.board[oldRow][oldCol]
        piece.coord = pos

    def removePieceInPosition(self, pos):
        row = pos[0]
        col = pos[1]
        self.board[row][col] = None

    def addPieceToPosition(self, piece, pos):
        row = pos[0]
        col = pos[1]
        self.board[row][col] = piece

    def makeMove(self, move):
        self.history.append(move)
        if move.kingsideCastle or move.queensideCastle:
            kingToMove = move.piece
            rookToMove = move.specialMovePiece
            self.movePieceToPosition(kingToMove, move.newPosition)
            self.movePieceToPosition(rookToMove, move.rookMove.newPosition)
            kingToMove.movesMade += 1
            rookToMove.movesMade += 1

        elif move.passant:
            pawnToMove = move.piece
            pawnToTake = move.specialMovePiece
            # pawnToMove.coord = move.newPosition
            self.removePieceInPosition(pawnToTake.coord)
            self.movePieceToPosition(pawnToMove, move.newPosition)
            pawnToMove.movesMade += 1

        elif move.promotion:
            pieceToTake = move.capturing
            piecePromoteTo = move.specialMovePiece
            self.removePieceInPosition(move.oldPosition)
            if pieceToTake:
                if pieceToTake.side == WHITE:
                    self.points -= pieceToTake.value
                elif pieceToTake.side == BLACK:
                    self.points += pieceToTake.value
                self.removePieceInPosition(pieceToTake.coord)

            self.addPieceToPosition(piecePromoteTo, piecePromoteTo.coord)
            if move.piece.side == WHITE:
                self.points += piecePromoteTo.value - 1
            elif move.piece.side == BLACK:
                self.points -= piecePromoteTo.value - 1
            move.piece.movesMade += 1

        else:  # normal move
            pieceToMove = move.piece
            pieceToTake = move.capturing

            if pieceToTake:
                if pieceToTake.side == WHITE:
                    self.points -= pieceToTake.value
                elif pieceToTake.side == BLACK:
                    self.points += pieceToTake.value
                self.removePieceInPosition(pieceToTake.coord)

            self.movePieceToPosition(pieceToMove, move.newPosition)
            pieceToMove.movesMade += 1

        self.movesMade += 1
        self.currentSide = not self.currentSide

    def undoLastMove(self):
        lastMove = self.history.pop()

        if lastMove.kingsideCastle or lastMove.queensideCastle:
            king = lastMove.piece
            rook = lastMove.specialMovePiece
            self.movePieceToPosition(king, lastMove.oldPosition)
            self.movePieceToPosition(rook, lastMove.rookMove.oldPosition)

            king.movesMade -= 1
            rook.movesMade -= 1

        elif lastMove.passant:
            pawnMoved = lastMove.piece
            pawnTaken = lastMove.specialMovePiece
            self.movePieceToPosition(pawnMoved, lastMove.oldPosition)
            self.addPieceToPosition(pawnTaken, pawnTaken.coord)
            pawnMoved.movesMade -= 1
            if pawnTaken.side == WHITE:
                self.points += 1
            else:
                self.points -= 1

        elif lastMove.promotion:
            pieceTaken = lastMove.capturing
            pieceMoved = lastMove.piece
            promotedPiece = lastMove.specialMovePiece
            # remove promoted piece
            self.removePieceInPosition(promotedPiece.coord)
            # add back original pawn
            self.addPieceToPosition(pieceMoved, pieceMoved.coord)
            if promotedPiece.side == WHITE:
                self.points -= promotedPiece.value - 1
            else:
                self.points += promotedPiece.value - 1

            if pieceTaken:
                if pieceTaken.side == WHITE:
                    self.points += pieceTaken.value
                else:
                    self.points -= pieceTaken.value
                # add back the taken piece
                self.addPieceToPosition(pieceTaken, pieceTaken.coord)

            pieceMoved.movesMade -= 1

        # undo normal move
        else:
            pieceMoved = lastMove.piece
            pieceTaken = lastMove.capturing

            self.movePieceToPosition(pieceMoved, lastMove.oldPosition)
            if pieceTaken:
                if pieceTaken == WHITE:
                    self.points += pieceTaken.value
                else:
                    self.points -= pieceTaken.value
                self.addPieceToPosition(pieceTaken, pieceTaken.coord)
            pieceMoved.movesMade -= 1

        self.currentSide = not self.currentSide

    def returnAllPiece(self):
        for row in range(8):
            for col in range(8):
                yield self.board[row][col]

    def getPointValueOfSide(self, side):
        points = 0
        for piece in self.returnAllPiece():
            # Materials
            if piece and piece.side == side:
                points += piece.value
                coord = piece.coord
                # if piece is black, mirror its coord for evaluation
                if piece.side == BLACK:
                    coord = self.getMirrorCoord(coord)
                points += self.getPSTValue(piece, coord)

        return points

    def getSidePointAdvantage(self, inspectSide):
        score = self.getPointValueOfSide(inspectSide) - self.getPointValueOfSide(not inspectSide)
        return score

    def evaluation(self, inspectSide):
        points = 0
        for piece in self.returnAllPiece():
            if piece:
                if piece.side == inspectSide:
                    points += self.getPieceValue(piece)
                else:
                    points -= self.getPieceValue(piece)
        return points

    def getPieceValue(self, piece):
        coord = piece.coord
        if piece.side == BLACK:
            coord = self.getMirrorCoord(coord)
        value = piece.value + self.getPSTValue(piece, coord)
        return value

    def getMirrorCoord(self, coord):
        return C(7 - coord[0], coord[1])

    def getPSTValue(self, piece, coord):
        return sqTable[piece.symbol][coord[0]][coord[1]]


# board = [["x", "x", "x", "x", "x", "x", "x", "x"],
#          ["x", "x", "x", "x", "x", "x", "x", "x"],
#          ["x", "x", "x", "x", "x", "x", "x", "x"],
#          ["x", "x", "x", "x", "x", "x", "x", "x"],
#          ["x", "x", "x", "x", "x", "x", "x", "x"],
#          ["x", "x", "x", "x", "x", "x", "x", "x"],
#          ["x", "x", "x", "x", "x", "x", "x", "x"],
#          ["x", "x", "x", "x", "x", "x", "x", "x"]]


if __name__ == "__main__":
    pass
    # b = Board()
    #
    # b.print_board()
    # print(b.evaluation(b.currentSide))
    # moves = list(b.getAllMoves(True))
    # print(moves)

    # print(b.pieceAtPosition((3,0)))
    # for i in range(8):
    #     for j in range(8):
    #         print(sqTable['k'][i][j], end=",")
    #     print()
