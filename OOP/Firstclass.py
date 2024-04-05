class Cuboid:
    def __init__(self, l, w, h):
        print(id(self)) #can ignore, just want to see the id 
        self.length = l
        self.width = w
        self.height = h

    def lidArea(self):
        return self.length * self.width

    def totalArea(self):
        return 2*(self.length* self.width + self.width * self.height + self.length * self.height)

    def volume(self):
        return self.length * self.width * self.height


c1 = Cuboid(10, 10, 67)

print("The lid area of C1 is: ",c1.lidArea())

c2= Cuboid(10, 66, 88)
print("The lid area of C2 is: ",c2.lidArea())


