from game import *

def alpha_beta(board, maximizing, alpha, beta):

    result = check_winner(board)

    if result == PLAYER_X:
        return 1

    if result == PLAYER_O:
        return -1

    if result == "DRAW":
        return 0

    if maximizing:

        value = -999

        for move in available_moves(board):

            value = max(
                value,
                alpha_beta(
                    make_move(board, move, PLAYER_X),
                    False,
                    alpha,
                    beta
                )
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:

        value = 999

        for move in available_moves(board):

            value = min(
                value,
                alpha_beta(
                    make_move(board, move, PLAYER_O),
                    True,
                    alpha,
                    beta
                )
            )

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


def best_move(board):

    best_score = -999
    best = None

    for move in available_moves(board):

        score = alpha_beta(
            make_move(board, move, PLAYER_X),
            False,
            -999,
            999
        )

        if score > best_score:
            best_score = score
            best = move

    return best
