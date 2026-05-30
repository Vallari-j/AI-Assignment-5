from game import *

MAX_DEPTH = 3


def evaluate(board):

    winner = check_winner(board)

    if winner == PLAYER_X:
        return 100

    if winner == PLAYER_O:
        return -100

    return 0


def heuristic_search(
        board,
        depth,
        maximizing,
        alpha,
        beta):

    winner = check_winner(board)

    if winner or depth == 0:
        return evaluate(board)

    if maximizing:

        value = -999

        for move in available_moves(board):

            value = max(
                value,
                heuristic_search(
                    make_move(board, move, PLAYER_X),
                    depth-1,
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
                heuristic_search(
                    make_move(board, move, PLAYER_O),
                    depth-1,
                    True,
                    alpha,
                    beta
                )
            )

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value
