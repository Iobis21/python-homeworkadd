# 3. Car კლასი


class Car:
    def __new__(cls, brand, model, year):
        print("Creating new car...")
        return super().__new__(cls)

    def __init__(self, brand, model, year):
        print("Initializing car...")
        self.brand = brand
        self.model = model
        self.year = year

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Brand must be a non-empty string")
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Model must be a non-empty string")
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Year must be an integer")
        if value < 1886 or value > 2026:
            raise ValueError("Year must be between 1886 and 2026")
        self._year = value

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


car = Car("Toyota", "Prius", 2015)
print(car)

car.year = 2020
car.model = "Camry"
print(car)

try:
    car.year = "2020"
except ValueError as error:
    print("Error:", error)

try:
    car.brand = ""
except ValueError as error:
    print("Error:", error)
