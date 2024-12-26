# class Student:
#     def __init__(self, roll, name):    #local parameter
#         print('this is a student')
#         self.name = name         #self.name = class instance
#         self.roll = roll
#     def showData(self):
#         print(f'the name is {self.name} and th roll no. is{self.roll}')
# a1 = Student(100, 'ram')
# a1.showData()

class Emp:
    def __init__(self, id, nm,sal):    #local parameter
        print('this is a Employee')
        self.id = id         #self.name = class instance
        self.name = nm
        self.salary = sal
    def showData(self):
        print(f'the id is {self.id}\n the name is{self.name}\n the salary is{self.salary}')

class Mgr(Emp):
    def __init__(self, id, nm, sal, allow):
        print('thia is manager')
        self.id = id
        self.name = nm
        self.salary = sal
        self.allowance = allow
    def showdata(self):  #overriding
        print(f'the id is {self.id}\n the name is{self.name}\n the salary is{self.salary}\n the allowns is{(self.salary * self.allowance)/100}')

E1 = Emp(100, 'ram', 60000)
M1 = Mgr(200, 'ram', 60000, 25)
E1.showData()
M1.showData