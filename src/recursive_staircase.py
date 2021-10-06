from functools import lru_cache

class RecursiveStaircase:
    @lru_cache()
    def solve(self, stair_num):
        if stair_num <= 0: return 0
        if stair_num == 1: return 1
        if stair_num == 2: return 2
        return self.solve(stair_num-1) + self.solve(stair_num-2)
if __name__ == '__main__':
    rs = RecursiveStaircase()
    rs.solve(100)