from abc import abstractmethod, ABC


class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def get_info(self):
        pass


class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def get_info(self):
        return f"Make : {self.make}, Model : {self.model}, Year : {self.year}, Battery Capacity : {self.battery_capacity}"


class GasCar(Vehicle):
    def __init__(self, make, model, year, fueltype):
        super().__init__(make, model, year)
        self.fueltype = fueltype

    def get_info(self):
        return f"Make : {self.make}, Model : {self.model}, Year : {self.year}, FuelType : {self.fueltype}"


class VehicleInventory:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def display(self):
        for car in self.cars:
            print(car.get_info())


if __name__ == "__main__":

    car1 = ElectricCar("Toyota", "Vios", 2021, 50)
    car2 = GasCar("Mitsubihshi", "Cronos", 2023, "Diesel")

    main = VehicleInventory()
    main.add_car(car1)
    main.add_car(car2)
    main.display()
