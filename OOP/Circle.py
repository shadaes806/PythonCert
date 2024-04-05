# student challenge
from math import *


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        res = pi * (self.radius ** 2)
        return res

    def perimeter(self):
        res = 2 * pi * self.radius
        return res


c1 = Circle(6)
c2 = Circle(7)
print(c1.area())
print(c2.area())