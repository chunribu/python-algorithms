# Rain Terraces (Trapping Rain Water) Problem
Given an array of non-negative integers representing terraces in an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
## Solutions
**Dynamic Programming** 

An element of array can store water if there are higher bars on left and right. We can find amount of water to be stored in every element by finding the heights of bars on left and right sides. The idea is to compute amount of water that can be stored in every element of array. For example, consider the array [3, 0, 0, 2, 0, 4], We can trap "3*2 units" of water between 3 an 2, "1 unit" on top of bar 2 and "3 units" between 2 and 4. We can iterate over the left and right parts again and again just to find the highest bar size up to that index. But, this could be stored. Voila, dynamic programming.

So we may pre-compute highest bar on left and right of every bar in O(n) time. Then use these pre-computed values to find the amount of water in every array element. 

**Implementation**

```python
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
```