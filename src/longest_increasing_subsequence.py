class LongestIncreasingSubsequence:
    def solve(self, array):
        lengths = [1 for i in range(len(array))]
        pre_idx, cur_idx = 0, 1
        while cur_idx < len(array):
            if array[pre_idx] < array[cur_idx]:
                cur_len = lengths[pre_idx] + 1
                if cur_len > lengths[cur_idx]:
                    lengths[cur_idx] = cur_len
            pre_idx += 1
            if pre_idx == cur_idx:
                cur_idx += 1
                pre_idx = 0
        return max(lengths)
# test
lis = LongestIncreasingSubsequence()
lis.solve([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])