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
# test
up = UniquePaths()
up.solve(7,3)