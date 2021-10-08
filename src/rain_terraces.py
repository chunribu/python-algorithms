class RainTerraces:
    def solve(self, terraces:list) -> int:
        max_from_left, max_from_right = [], []
        n = len(terraces)
        for i in range(n):
            last_from_left = 0 if len(max_from_left)==0 else max_from_left[-1]
            max_from_left.append(max(last_from_left, terraces[i]))
            last_from_right = 0 if len(max_from_right)==0 else max_from_right[-1]
            max_from_right.append(max(last_from_right, terraces[n-1-i]))
        max_from_right.reverse()
        water_amount = [min(max_from_left[i], max_from_right[i])-terraces[i] for i in range(n)]
        return sum(water_amount)
# test
rt = RainTerraces()
rt.solve([3, 0, 0, 2, 0, 4])