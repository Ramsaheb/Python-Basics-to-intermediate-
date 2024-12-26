class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromstr(cls, string):
        return cls(string.split('-')[0], string.split('-')[1])

string = 'ram-199999'   
e1 = Employee.fromstr(string)
print(e1.name, e1.salary)