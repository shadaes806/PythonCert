def PetLover(pet):
    pet.talk()
    pet.walk()


class Duck:
    def talk(self):
        print('Duck is talking')

    def walk(self):
        print('Duck is walking')


class Dog:
    def talk(self):
        print('Dog is talking')

    def walk(self):
        print('Dg is walking')


d = Duck()

PetLover(d)
