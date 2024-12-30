#for removing the things like this 
#my_car.model = "Ram"
#result = print(my_car.model) ==> Ram 


class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1  

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"  

    @staticmethod
    def general_descriptions():
        return "Cars are sexier than the girls" 
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_car = Car("Toyota", "Corolla")

my_tesla = ElectricCar("tesla", "model S", "85 kWH")



 
#print(isinstance(my_tesla, Car))        
# print(isinstance(my_tesla, ElectricCar))

# my_car.model = "Ram"
# print(my_car.model)

# print(Car.general_descriptions())
# print(my_car.general_descriptions())