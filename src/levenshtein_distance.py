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
    def show(self):
        if hasattr(self, 'distance'):
            dist = self.distance
            for x in range(-1,len(a)):
                row = []
                for y in range(-1, len(b)):
                    row.append(dist[(x,y)])
                print(row)
# test
ld = LevenshteinDistance()
ld.solve('kitten','sitting')
ld.show()