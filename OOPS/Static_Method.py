class A:
    def __init__(self, num):
        self.num = num
    def addNum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b
    
a = A(5)
a.addNum(6)
print(a.num)
