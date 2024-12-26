class A:
    def __init__(self):
        self.__name = 'ram'
a = A()
# print(a.__name)
# name mangling
print(a._A__name)