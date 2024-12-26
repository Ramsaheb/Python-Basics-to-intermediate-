class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print_area(self):
        return self.x * self.y
    
class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
        super().__init__(l, b)
    def area(self):
        return super().print_area()
    
r = Rectangle(4, 5)
print(r.area())