board = [[None, None, None],[None, None, None],[None, None, None]]
player1 = input("Enter the name of the player who wants to play as 0 : ")
player2 = input("Enter the name of the player who wants to play as X : ")
winner = None
def print_board(board):
    print("The current board status is: ", end="\n")
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(str(board[i][j]), end= "  ")
        print("\n")

def play():
    global winner
    while winner is None:
        print_board(board)
        move = input("Player %s: input your move like this [row][col]: " % player1)
        row = int(move[0])
        col = int(move[1])
        board[row][col] = str("0")
        print("Input Recorded")
        if check_winner(board) == player1:
            print_board(board)
            print("Congratulations %s! You Won the Game" % player1)
            exit(0)
        else:
            print_board(board)
            move = input("Player %s: input your move like this [row][col]: " % player2)
            row = int(move[0])
            col = int(move[1])
            board[row][col] = str("X")
            if check_winner(board) == player2:
                print_board(board)
                print("Congratulations %s! You Won the Game" % player2)
                exit(0)

def check_winner(board):
    global winner
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            winner = player2

        elif board[0][0] == "0":
            winner = player1

    elif board[0][0] == board[0][1] == board[0][2]:
        if board[0][0] == "X":
            winner = player2

        elif board[0][0] == "0":
            winner = player1

    elif board[1][0] == board[1][1] == board[1][2]:
        if board[1][0] == "X":
            winner = player2

        elif board[1][0] == "0":
            winner = player1

    elif board[2][0] == board[2][1] == board[2][2]:
        if board[2][0] == "X":
            winner = player2

        elif board[2][0] == "0":
            winner = player1

    elif board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] == "X":
            winner = player2

        elif board[0][0] == "0":
            winner = player1

    elif board[0][1] == board[1][1] == board[2][1]:
        if board[0][1] == "X":
            winner = player2

        elif board[0][1] == "0":
            winner = player1

    elif board[0][2] == board[1][2] == board[2][2]:
        if board[0][2] == "X":
            winner = player2

        elif board[0][2] == "0":
            winner = player1
    return winner



if __name__ == "__main__":
    play()
