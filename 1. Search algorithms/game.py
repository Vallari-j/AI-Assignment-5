EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"


def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])


def available_moves(board):
    return [i for i in range(9) if board[i] == EMPTY]


def make_move(board, move, player):
    new_board = board[:]
    new_board[move] = player
    return new_board


def check_winner(board):

    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in wins:
        a,b,c = combo

        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]

    if EMPTY not in board:
        return "DRAW"

    return None
