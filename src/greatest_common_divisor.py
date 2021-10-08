class GreatestCommonDivisor:
    def solve(self, num_a, num_b):
        a, b = abs(num_a), abs(num_b)
        return a if b==0 else self.solve(b, a%b)
# test
gc = GreatestCommonDivisor()
gc.solve(252, 105)