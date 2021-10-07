# Unique Paths Problem
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

**Example 1**
```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
```

**Example 2**
```
Input: m = 7, n = 3
Output: 28
```

## Solutions

**Dynamic Programming**

Let's treat `BOARD[i][j]` as our sub-problem.

Since we have restriction of moving only to the right and down we might say that number of unique paths to the current cell is a sum of numbers of unique paths to the cell above the current one and to the cell to the left of current one.
```
BOARD[i][j] = BOARD[i - 1][j] + BOARD[i][j - 1]
```

Base cases are:
```
BOARD[0][any] = 1; // only one way to reach any top slot.
BOARD[any][0] = 1; // only one way to reach any slot in the leftmost column.
```

### Implementation
```python
class UniquePaths:
    def solve(self, rows, cols):
        board = [[0 for j in range(cols)] for i in range(rows)]
        for x in range(rows):
            for y in range(cols):
                if x==0 or y==0:
                    board[x][y] = 1
                else:
                    board[x][y] = board[x-1][y] + board[x][y-1]
        return board[x][y]
```