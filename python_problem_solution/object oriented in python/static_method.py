class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1  

    def fuel_type(self):
        return "Petrol or Diesel"  

    @staticmethod
    def general_descriptions():
        return "Cars are sexier than the girls" 

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_car = Car("Toyota", "Corolla")


my_tesla = ElectricCar("tesla", "model S", "85 kWH")


print(Car.general_descriptions())
print(my_car.general_descriptions())

