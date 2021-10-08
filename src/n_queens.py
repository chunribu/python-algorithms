class NQueens:
    def __init__(self, queens_count):
        self.queens_count = queens_count
        self.solutions = []
    def is_safe(self, positions, row, col):
        if positions == []: return True
        for y, x in enumerate(positions):
            if x==row: return False
            if abs(x-row) == abs(y-col): return False
        return True
    def recursive(self, col, positions=[]):
        if col == self.queens_count: 
            self.solutions.append(positions)
            return True
        for row in range(self.queens_count):
            if self.is_safe(positions, row, col):
                self.recursive(col+1, positions+[row])
        return False
    def solve(self):
        self.recursive(0)
        return len(self.solutions)
    def show(self):
        n = self.queens_count
        for idx, s in enumerate(self.solutions):
            chessboard = [['·']*n for i in range(n)]
            for c, r in enumerate(s): chessboard[r][c] = 'Q'
            print(f'Solution NO. {idx+1}:')
            for i in chessboard: print(' '.join(i))
# test
nq = NQueens(8)
nq.solve()
nq.show()