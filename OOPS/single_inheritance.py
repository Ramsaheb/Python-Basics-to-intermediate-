class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print('sound made by Animal')


class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def sound(self):
        print('Bark!!!!!')

d = Dog('moti')
d.sound()

a = Animal('kalu')
a.sound()