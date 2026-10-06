import sys
from datetime import datetime

# რომ ქართული ტექსტი ტერმინალში ჩანდეს
sys.stdout.reconfigure(encoding="utf-8")


# 1. Car კლასი
class Car:
    # 4. მანქანების რაოდენობა
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.number_of_cars += 1

    # 2. მანქანის ასაკი
    def age_of_car(self):
        return datetime.now().year - self.year

    def car_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Age:", self.age_of_car())

    # 5. სულ რამდენი მანქანაა
    @classmethod
    def total_cars(cls):
        print("Total cars:", cls.number_of_cars)


# 3. ElectricCar კლასი
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"ელემენტის ხანგრძლივობა შეადგენს {self.battery_life} საათს")


car1 = Car("Toyota", "Corolla", 2015)
car2 = Car("BMW", "X5", 2020)
tesla = ElectricCar("Tesla", "Model 3", 2022, 12)

car1.car_info()
print()
car2.car_info()
print()
tesla.car_info()
tesla.battery_info()
print()

Car.total_cars()
