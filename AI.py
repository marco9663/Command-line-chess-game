from Board import Board

WHITE = True
BLACK = False


class AI:
    def __init__(self, board, side, depth):
        self.board = board
        self.side = side
        self.depthLimit = depth

    def minimaxRoot(self, depth, isMaximizing):
        moves = self.board.getAllMoves(self.board.currentSide)
        bestMoveScore = -9999
        bestMove = None
        for move in moves:
            self.board.makeMove(move)
            # first level choose max
            value = self.minimax(move, depth - 1, -10000, 10000, not isMaximizing)

            self.board.undoLastMove()
            if value >= bestMoveScore:

                bestMoveScore = value
                bestMove = move
        return bestMove

    def minimax(self, move, depth, alpha, beta, isMaximizing):
        if depth == 0:
            return self.board.evaluation(self.side)
        moves = self.board.getAllMoves(self.board.currentSide)

        if isMaximizing:
            bestMoveScore = -9999
            for move in moves:
                self.board.makeMove(move)
                bestMoveScore = max(bestMoveScore, self.minimax(move, depth - 1, alpha, beta, not isMaximizing))
                self.board.undoLastMove()
                alpha = max(alpha, bestMoveScore)
                if alpha >= beta:
                    return bestMoveScore
            return bestMoveScore
        else:
            bestMoveScore = 9999
            for move in moves:
                self.board.makeMove(move)
                bestMoveScore = min(bestMoveScore, self.minimax(move, depth - 1, alpha, beta, not isMaximizing))
                self.board.undoLastMove()
                beta = min(beta, bestMoveScore)
                if beta <= alpha:
                    return bestMoveScore
            return bestMoveScore

    def getBestMove(self):
        return self.minimaxRoot(self.depthLimit, True)


if __name__ == "__main__":
    mainBoard = Board(passant=True)
    ai = AI(mainBoard, BLACK, 4)
    mainBoard.print_board()
    best = ai.minimaxRoot(4, WHITE)
    print(best)
    # mainBoard.print_board()
