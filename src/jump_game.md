# Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

We call a position in the array a "good index" if starting at that position, we can reach the last index. Otherwise, that index is called a "bad index". The problem then reduces to whether or not index 0 is a "good index".

**Example 1**

```
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```
**Example 2**

```
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
```

## Solutions
**Greedy**

Once we have our code in the bottom-up state, we can make one final, important observation. From a given position, when we try to see if we can jump to a GOOD position, we only ever use one - the first one. In other words, the left-most one. If we keep track of this left-most GOOD position as a separate variable, we can avoid searching for it in the array. Not only that, but we can stop using the array altogether.

### Implementation
```python
class JumpGame:
    def solve(self, array):
        n = len(array) 
        good_idx = n - 1 
        for i in range(n-2, -1, -1):
            if array[i] + i >= good_idx:
                good_idx = i 
        return good_idx == 0
```