# nd polymorphism

def Driver(car):
    car.drive()


class Creta:
    def drive(self):
        print('Creta is driving')


class Mercedes:
    def drive(self):
        print("mercedes is driving")


c = Creta()

Driver(c)
