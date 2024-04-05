# Method resolution Order

class A:
    def show(self):
        print('A')
class B:
    def show(self):
        print('b')


class C(B, A ):
    pass


c = C()
c.show()
print(c.mro())