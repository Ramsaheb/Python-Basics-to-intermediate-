class Car:
    def __init__(self, brand, model):
        self.__brand = brand #for making things private use "__"
        self.model = model
    
    def get_brand(self):
        return self.__brand  #getter

# just like setter is also there 
#       class MyClass:
#     def __init__(self):
#         self._my_property = None  # Private attribute

#     @property
#     def my_property(self):
#         return self._my_property

#     @my_property.setter
#     def my_property(self, value):
#         self._my_property = value

# # Usage
# obj = MyClass()
# obj.my_property = 10  # Setting the property value
# print(obj.my_property)  # Getting the property value

    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
my_tesla = ElectricCar("tesla", "model S", "85 kWH")
# print(my_tesla.brand, my_tesla.model,"with monster battery", my_tesla.battery_size)       
print(my_tesla.get_brand())