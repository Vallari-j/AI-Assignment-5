# Search Algorithms Implementation

## Objective

Implement and compare:

1. Minimax
2. Alpha-Beta Pruning
3. Heuristic Alpha-Beta Search
4. Monte Carlo Tree Search

using Tic-Tac-Toe.

---

## Algorithms

### Minimax

Exhaustively searches all game states.

Time Complexity:
O(b^d)

where:

b = branching factor
d = depth

---

### Alpha-Beta Search

Improves Minimax by pruning branches that
cannot affect the final decision.

Worst Case:
O(b^d)

Best Case:
O(b^(d/2))

---

### Heuristic Alpha-Beta

Uses:

- depth limit
- evaluation function

to handle larger search spaces.

---

### Monte Carlo Tree Search

Four phases:

1. Selection
2. Expansion
3. Simulation
4. Backpropagation

Approximates optimal decisions through
random simulations.

---

## Test Case

Board:

X X _
O O _
_ _ _

Expected move:

Position 2

Results:

Minimax -> 2
Alpha Beta -> 2
MCTS -> 2

Correctly identifies winning move.
