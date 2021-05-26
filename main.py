from Board import Board
from Input import InputParser
from AI import AI

WHITE = True
BLACK = False


def askForPlayerSide():
    choice = input("Please the side you want to play as [w/b]: ").lower()
    while choice != "w" and choice != "b":
        print("Value not valid. Please enter again.")
        choice = input("Please the side you want to play as [w/b]: ").lower()

    if choice == "w":
        print("You will play as white")
        return True
    else:
        print("You will play as black")
        return False


def askForNumPlayer():
    choice = int(input("Please the number of player [1/2]: "))
    while choice != 1 and choice != 2:
        print("Value not valid. Please enter again.")
        choice = int(input("Please the number of player [1/2]: "))

    if choice == 1:
        print("Game Mode: Single Player Mode")
        return True
    else:
        print("Game Mode: Two Player Mode")
        return False


def makeMove(move, board):
    print(move)
    board.makeMove(move)


def twoPlayerGame(board):
    parserWhite = InputParser(WHITE, board)
    parserBlack = InputParser(BLACK, board)
    kingDead = False
    while True:
        print()
        board.print_board()
        print()

        if board.currentSide == WHITE:
            side = "Black"
            opponent = "White"
        else:
            side = "White"
            opponent = "Black"

        if kingDead:
            print(f"{side}'s king is dead")
            print(f"{opponent} wins!")
            return

        if board.isCheckmate():
            print("Checkmate")
            print(f"{opponent} wins!")
            return

        if board.isStalemate():
            print("Stalemate")
            print("Draw")

        if board.currentSide == WHITE:
            parser = parserWhite
        else:
            parser = parserBlack
        move = None
        if board.currentSide == WHITE:
            side = "white"
        else:
            side = "black"

        command = input(f"It is {side}'s move. Type your move in e.g.(a6 d3).")
        if command == "u":
            board.undoLastMove()
            continue
        moveFrom = command[:2]
        moveTo = command[3:5]
        move = parser.moveParser(board.currentSide, moveFrom, moveTo)
        while not move:
            print("Input is not valid! Please enter again")
            command = input(f"It is {side}'s move. Type your move in e.g.(a6 d3).")
            moveFrom = command[:2]
            moveTo = command[3:5]
            move = parser.moveParser(board.currentSide, moveFrom, moveTo)

        makeMove(move, board)
        if move.capturing and move.capturing.symbol == "k":
            kingDead = True


def askForDepthOfAI():
    depthInput = int(input('How deep should the AI look for moves? '))
    return depthInput


def singlePlayerGame(board, playerSide, ai):
    parser = InputParser(playerSide, board)
    while True:
        print()
        board.print_board()
        print()

        if board.isCheckmate():
            if board.currentSide == playerSide:
                print("Checkmate, you lost")
            else:
                print("Checkmate! You won!")
            return

        if board.isStalemate():
            if board.currentSide == playerSide:
                print("Stalemate")
            else:
                print("Stalemate")
            return

        if board.currentSide == playerSide:
            command = input(f"It is your move. Type your move in e.g.(a6 d3).")
            if command == "u":
                board.undoLastMove()
                continue
            moveFrom = command[:2]
            moveTo = command[3:5]
            move = parser.moveParser(board.currentSide, moveFrom, moveTo)
            while not move:
                print("Input is not valid! Please enter again")
                command = input(f"It is your move. Type your move in e.g.(a6 d3).")
                moveFrom = command[:2]
                moveTo = command[3:5]
                move = parser.moveParser(board.currentSide, moveFrom, moveTo)

            makeMove(move, board)
        else:
            print("AI thinking...")
            move = ai.getBestMove()
            makeMove(move, board)


board = Board()

# ask for number of player
if askForNumPlayer():
    # For Single Player vs AI
    playerSide = askForPlayerSide()
    aiDepth = askForDepthOfAI()
    opponentAI = AI(board, not playerSide, aiDepth)
    singlePlayerGame(board, playerSide, opponentAI)

else:
    # For Two Player
    twoPlayerGame(board)
