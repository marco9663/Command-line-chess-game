from Coordinate import Coordinate as C

coordinate_x_dict = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7

}

coordinate_y_dict = {
    "1": 7,
    "2": 6,
    "3": 5,
    "4": 4,
    "5": 3,
    "6": 2,
    "7": 1,
    "8": 0

}


def stringToCoordinate(pos):
    try:
        x, y = [c for c in pos]
        return C(coordinate_y_dict[y], coordinate_x_dict[x])
    except KeyError:
        print(KeyError)


def coordinateToString(coord):
    col = chr(ord(str(coord[1])) - ord(str(0)) + ord("a"))
    row = str(8 - coord[0])
    return col + row


class InputParser:
    def __init__(self, side, board):
        self.side = side
        self.board = board

    def moveParser(self, side, oldPos_str, newPos_str):
        oldPos = stringToCoordinate(oldPos_str)
        newPos = stringToCoordinate(newPos_str)
        move = self.matchMovePos(side, oldPos, newPos)
        if move:
            return move

    def matchMovePos(self, side, oldPos, newPos):
        piece = self.board.pieceAtPosition(oldPos)
        promoteMove = self.board.mustPawnPromote(piece, newPos)
        moves = self.board.getPosPieceMove(oldPos)
        if promoteMove:
            promoteTo = input("Pawn promote to (q/r/n/b): ")
        for move in moves:
            if newPos == move.newPosition and move.piece.side == side:
                if promoteMove:
                    if move.specialMovePiece.symbol == promoteTo:
                        return move
                else:
                    return move

