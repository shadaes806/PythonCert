def add3(x, y, z):
    print('inside function ',id(x), id(y), id(z))


a, b, c = 10, 15, 5

print('outside function ', id(a), id(b), id(c))
print(add3(a, b, c))