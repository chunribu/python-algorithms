class MaximumSubarray:
    def solve(self, array):
        sum_list = [array[0]]
        start_idx = 0
        for i in range(1, len(array)):
            ele = array[i]
            addup = sum_list[-1] + ele
            sum_list.append(max(ele, addup))
            if ele > addup: start_idx = i
        max_sum = max(sum_list)
        end_idx = len(sum_list)-1 - sum_list[::-1].index(max_sum)
        print(array[start_idx:end_idx+1])
        return max_sum

# test
ms = MaximumSubarray()
ms.solve([-2, 1, -3, 4, -1, 2, 1, -5, 4])