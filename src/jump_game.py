class JumpGame:
    def solve(self, array):
        n = len(array) 
        good_idx = n - 1 
        for i in range(n-2, -1, -1):
            if array[i] + i >= good_idx:
                good_idx = i 
        return good_idx == 0
# test
jg = JumpGame()
jg.solve([[3,2,1,0,4]])