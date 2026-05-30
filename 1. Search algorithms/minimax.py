from game import *

def minimax(board, maximizing):
    result = check_winner(board)
    if result == PLAYER_X:
        return 1

    if result == PLAYER_O:
        return -1

    if result == "DRAW":
        return 0

    if maximizing:

        best = -999

        for move in available_moves(board):

            score = minimax(
                make_move(board, move, PLAYER_X),
                False
            )

            best = max(best, score)

        return best

    else:

        best = 999

        for move in available_moves(board):

            score = minimax(
                make_move(board, move, PLAYER_O),
                True
            )

            best = min(best, score)

        return best


def best_move(board):

    best_score = -999
    move_choice = None

    for move in available_moves(board):

        score = minimax(
            make_move(board, move, PLAYER_X),
            False
        )

        if score > best_score:
            best_score = score
            move_choice = move

    return move_choice
