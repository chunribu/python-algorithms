# Recursive Staircase Problem
There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 or 2 stairs at a time. Count the number of ways, the person can reach the top.

## Solutions
**Recursive Solution With Memoization**

There are two ways to stair n at a time:
    a) from stair n-1 in one step or
    b) from stair n-2 in two steps.
Specially, there is:
    a) 1 way to stair 1 and
    b) 2 ways to stair 2.

**Implementation**

```python
from functools import lru_cache

class RecursiveStaircase:
    @lru_cache()
    def solve(self, stair_num):
        if stair_num <= 0: return 0
        if stair_num == 1: return 1
        if stair_num == 2: return 2
        return self.solve(stair_num-1) + self.solve(stair_num-2)
```