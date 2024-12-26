class Parent:
    def parentclass(self):
        print('this is the parent class')

class Child(Parent):
    def childclass(self):
        print('this is the child class')
        super().parentclass()

child_object = Child()
child_object.childclass()
