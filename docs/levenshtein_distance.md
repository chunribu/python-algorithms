# Levenshtein Distance
The Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other.

For example, the Levenshtein distance between "kitten" and "sitting" is 3, since the following three edits change one into the other, and there is no way to do it with fewer than three edits:
+ kitten → sitten (substitution of "s" for "k")
+ sitten → sittin (substitution of "i" for "e")
+ sittin → sitting (insertion of "g" at the end).

## Solutions
**Dynamic Programming**

### Implementation
```python
class LevenshteinDistance:
    def solve(self, str_a, str_b):
        a, b = str_a, str_b
        dist = {(x,y):0 for x in range(len(a)) for y in range(len(b))}
        for x in range(len(a)): dist[(x,-1)] = x+1
        for y in range(len(b)): dist[(-1,y)] = y+1
        dist[(-1,-1)] = 0
        for i in range(len(a)):
            for j in range(len(b)):
                need_edit = a[i]!=b[j]
                last_edits = min(dist[(i,j-1)], dist[(i-1,j)], dist[(i-1,j-1)])
                dist[(i,j)] = last_edits + int(need_edit)
        self.distance = dist
        return dist[(i,j)]
```