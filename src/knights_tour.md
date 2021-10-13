# Knight's Tour

A **knight's tour** is a sequence of moves of a knight on a chessboard 
such that the knight visits every square only once. If the knight 
ends on a square that is one knight's move from the beginning 
square (so that it could tour the board again immediately, 
following the same path), the tour is **closed**, otherwise it 
is **open**.

The **knight's tour problem** is the mathematical problem of 
finding a knight's tour. Creating a program to find a knight's 
tour is a common problem given to computer science students.
Variations of the knight's tour problem involve chessboards of 
different sizes than the usual `8×8`, as well as irregular 
(non-rectangular) boards.

## Solutions

**Backtracking**

### Implementation

```python
class KnightsTour:
    def solve(self, chessboard_size):
        n = chessboard_size
        chessboard = {(x,y):0 for y in range(n) for x in range(n)}
        moves = []
        first_move = (0, 0)
        moves.append(first_move)
        chessboard[first_move] = 1
        solution_was_found = self.recursive(chessboard, moves, chessboard_size)
        return moves if solution_was_found else []
    def recursive(self, chessboard, moves, chessboard_size):
        if self.is_tour_over(chessboard, moves):
            return True
        last_move = moves[len(moves)-1]
        possible_moves = self.get_possible_moves(chessboard_size, last_move)
        for move in possible_moves:
            if self.is_move_allowed(chessboard, move):
                moves.append(move)
                chessboard[move] = 1
                if self.recursive(chessboard, moves, chessboard_size):
                    return True
                moves.pop()
                chessboard[move] = 0
        return False
    def get_possible_moves(self, chessboard_size, position):
        all_moves = [
            (position[0] - 1, position[1] - 2),
            (position[0] - 2, position[1] - 1),
            (position[0] + 1, position[1] - 2),
            (position[0] + 2, position[1] - 1),
            (position[0] - 2, position[1] + 1),
            (position[0] - 1, position[1] + 2),
            (position[0] + 1, position[1] + 2),
            (position[0] + 2, position[1] + 1)
        ]
        n = chessboard_size
        possible_moves = [m for m in all_moves if \
            m[0]>=0 and m[1]>=0 and m[0]<n and m[1]<n]
        return possible_moves

    def is_tour_over(self, chessboard, moves):
        return len(chessboard) == len(moves)

    def is_move_allowed(self, chessboard, move):
        return chessboard[move] != 1
```