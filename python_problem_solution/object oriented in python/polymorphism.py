#single method used in both like fuel types

class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1  

    def fuel_type(self):
        return "Petrol or Diesel"   

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_car = Car("Toyota", "Corolla")
print(my_car.fuel_type())

my_tesla = ElectricCar("tesla", "model S", "85 kWH")
print(my_tesla.fuel_type())


print(Car.total_car)