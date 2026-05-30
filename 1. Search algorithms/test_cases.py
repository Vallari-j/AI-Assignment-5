from minimax import best_move as minimax_move
from alpha_beta import best_move as alpha_move
from monte_carlo_tree_search import mcts_move

board = [
    "X","X"," ",
    "O","O"," ",
    " "," "," "
]

print("Winning move should be position 2")

print(
    "Minimax:",
    minimax_move(board)
)

print(
    "Alpha Beta:",
    alpha_move(board)
)

print(
    "MCTS:",
    mcts_move(board)
)
