class Myclass:
    def __init__(self, value):
        self._value = value    #protected
    
    def show(self):
        print(f'the value is {self._value}')

    @property
    def ten_val(self):          # getter
        return 10 * self._value
    
    @ten_val.setter
    def ten_val(self, new_val):
        self._value = new_val / 10

obj = Myclass(10)
obj.ten_val = 99
print(obj.ten_val)
obj.show()