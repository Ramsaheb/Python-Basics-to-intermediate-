class Employee:
    company = 'Openai'
    def showInfo(self, name):
        self.name = name
        print(f'the name is {self.name} and the company name is {self.company}')
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.showInfo('Ram')
e1.changeCompany('Tesla')
e1.showInfo('Ram')
print(Employee.company)

