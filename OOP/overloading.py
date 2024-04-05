class Arith:
    def sum(self, a, b, c=None):
        s = a + b
        if c == None:
            return s
        else:
            return s + c


a = Arith()

print(a.sum(9, 8))
print(a.sum('hello', 'wall', 'kill'))
