import random
from game import *


def random_playout(board, player):

    current = player
    state = board[:]

    while True:

        winner = check_winner(state)

        if winner:
            return winner

        move = random.choice(
            available_moves(state)
        )

        state[move] = current

        current = (
            PLAYER_O
            if current == PLAYER_X
            else PLAYER_X
        )


def mcts_move(board, simulations=500):

    moves = available_moves(board)

    scores = {}

    for move in moves:

        wins = 0

        for _ in range(simulations):

            new_board = make_move(
                board,
                move,
                PLAYER_X
            )

            result = random_playout(
                new_board,
                PLAYER_O
            )

            if result == PLAYER_X:
                wins += 1

            elif result == "DRAW":
                wins += 0.5

        scores[move] = wins

    return max(scores, key=scores.get)
