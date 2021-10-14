# Regular Expression Matching

Given an input string `s` and a pattern `p`, implement regular 
expression matching with support for `.` and `*`.

- `.` Matches any single character.
- `*` Matches zero or more of the preceding element.

The matching should cover the **entire** input string (not partial).

**Note**

- `s` could be empty and contains only lowercase letters `a-z`.
- `p` could be empty and contains only lowercase letters `a-z`, and characters like `.` or `*`.

**Example 1**

Input:
```
s = 'aa'
p = 'a'
```

Output: `false`

Explanation: `a` does not match the entire string `aa`.

**Example 2**

Input:
```
s = 'aa'
p = 'a*'
```

Output: `true`

Explanation: `*` means zero or more of the preceding element, `a`. 
Therefore, by repeating `a` once, it becomes `aa`.

**Example 3**

Input:

```
s = 'ab'
p = '.*'
```

Output: `true`

Explanation: `.*` means "zero or more (`*`) of any character (`.`)".

**Example 4**

Input:

```
s = 'aab'
p = 'c*a*b'
```

Output: `true`

Explanation: `c` can be repeated 0 times, `a` can be repeated 
1 time. Therefore it matches `aab`.

## Solutions

**Dynamic Programming**

### Implementation

```python
class RegularExpressionMatching:
    def __init__(self):
        self.zero_or_more_char = '*'
        self.any_char = '.'
    def solve(self, string, pattern):
        rows = range(len(string)+1)
        cols = range(len(pattern)+1)
        match_matrix = {(i, j): None for i in rows for j in cols}
        match_matrix[(0,0)] = True
        for j in cols:
            if j==0: continue
            if pattern[j-1] == self.zero_or_more_char:
                match_matrix[(0,j)] = match_matrix[(0,j-2)]
            else:
                match_matrix[(0,j)] = False
        for i in rows:
            if i==0: continue
            match_matrix[(i,0)] = False
        for i in rows:
            if i==0: continue
            for j in cols:
                if j==0: continue
                str_idx, ptn_idx = i-1, j-1
                if pattern[ptn_idx] == self.zero_or_more_char:
                    if match_matrix[(i, j-2)] == True:
                        match_matrix[(i,j)] = True
                    elif (pattern[ptn_idx-1] == string[str_idx] or \
                        pattern[ptn_idx-1] == self.any_char) and \
                            match_matrix[(i-1, j)] == True:
                        match_matrix[(i, j)] = True
                    else: match_matrix[(i,j)] = False
                elif pattern[ptn_idx] == string[str_idx] or \
                    pattern[ptn_idx] == self.any_char:
                    match_matrix[(i,j)] = match_matrix[(i-1, j-1)]
                else:
                    match_matrix[(i,j)] = False
        return match_matrix[(len(string), len(pattern))]
```