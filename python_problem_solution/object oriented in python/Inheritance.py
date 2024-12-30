class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
my_tesla = ElectricCar("tesla", "model S", "85 kWH")
print(my_tesla.brand, my_tesla.model,"with monster battery", my_tesla.battery_size)