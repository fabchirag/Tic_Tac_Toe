import numpy

# Three rows, within each row needs to be separate list
board = numpy.array([["-", "-", "-"],["-", "-", "-"], ["-", "-", "-"]])
player1 = "X"
player2 = "O"


def check_rows(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board [r][c] == symbol:
                count = count + 1
        if count == 3:
            print(symbol, "won")
            return True
    return False

def check_columns(symbol):
    for c in range(3):
        count = 0
        for r in range(3):
            if board [r][c] == symbol:
                count = count + 1
        if count == 3:
            print(symbol, "won")
            return True
    return False


def check_diagonals(symbol):
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] == symbol:
        print(symbol, "won")
        return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] == symbol:
        print(symbol, "won")
        return True
    return False




def won(symbol):
    return check_rows(symbol) or check_column(symbol) or check_diagonals(symbol)



def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row = int(input("Enter row - 1 or 2 or 3: "))
        column = int(input("Enter column -1 or 2 or 3: "))
        if row > 0 and row < 4 and column > 0 and column < 4 and board[row-1][column-1]=="-":
            break
        else:
            print("Invalid input. Please enter again")
    board[row-1][column-1] = symbol




def play():
    for turn in range(9):
        """ If its an even turn e.g. 2, 4, 6 then its player 1 turn."""
        if turn % 2 == 0:
            print("X turn")
            place(player1) # This allows player 1 to place a symbol on the board
            if won(player1):
                break
        else:
            print("O turn")
            place(player2)  # This allows player 1 to place a symbol on the board
            if won(player2):
                break

    if not(won(player1)) and not(won(player2)):
        print("Draw")



