from abc import ABC, abstractmethod
from typing import List


class Vehicle(ABC):
    def __init__(self, make: str, model: str, year: int, color: str, code: str):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.code = code

    @abstractmethod
    def get_details(self) -> str:
        pass


class Car(Vehicle):
    def __init__(self, make, model, year, color, code, price):
        super().__init__(make, model, year, color, code)
        self.price = price

    def get_details(self):
        return f"{self.make} {self.model} ({self.year}) - Color: {self.color}, Code: {self.code}, Price: {self.price}"


class ElectricCar(Car):
    def __init__(self, make, model, year, color, code, price, battery_capacity):
        super().__init__(make, model, year, color, code, price)
        self.battery = battery_capacity

    def get_details(self):
        base = super().get_details()
        return f"{base}, Battery: {self.battery}kWh"


class GasCar(Car):
    def __init__(self, make, model, year, color, code, price, fuel_type):
        super().__init__(make, model, year, color, code, price)
        self.fuel_type = fuel_type

    def get_details(self):
        base = super().get_details()
        return f"{base}, Fuel Type: {self.fuel_type}"


class Customer:
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id
        self.wallet = 0
        self.cars: List[Car] = []
        self.registered = False

    def cash_in(self, amount: float):
        if amount > 0:
            self.wallet += amount
            return f"Added {amount} to wallet."
        return "Invalid amount"

    def rent_car(self, car: Car, pay: float):
        if pay < car.price:
            return "Not enough funds."
        if self.wallet < pay:
            return "Insufficient wallet balance."

        self.wallet -= pay
        self.cars.append(car)
        return f"Rented car: {car.make} {car.model}"

    def return_car(self, car: Car, rental: "CarRental"):
        if car in self.cars:
            self.cars.remove(car)
            rental.cars.append(car)
            return f"Returned {car.make} {car.model}"
        return "Car not in customer's list"

    def get_details(self):
        rented = ", ".join([car.make for car in self.cars]) if self.cars else "None"
        return f"Customer: {self.name}, ID: {self.id}, Wallet: {self.wallet}, Rented Cars: {rented}"


class CarRental:
    def __init__(self, name: str, location: str, owner: str):
        self.name = name
        self.location = location
        self.owner = owner
        self.cars: List[Car] = []
        self.customers: List[Customer] = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def remove_car(self, code: str):
        for car in self.cars:
            if car.code == code:
                self.cars.remove(car)
                return f"Removed {car.make} with code {code}"
        return "Car not found"

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return "Already registered"
        self.customers.append(customer)
        customer.registered = True
        return f"{customer.name} is now registered."

    def give_car(self, customer: Customer, code: str, pay: float):
        if not customer.registered:
            return "Customer not registered."

        for car in self.cars:
            if car.code == code:
                result = customer.rent_car(car, pay)
                if "Rented" in result:
                    self.cars.remove(car)
                return result
        return "Car code not found."

    def display_customers(self):
        for cust in self.customers:
            print(cust.get_details())

    def display_cars(self):
        if not self.cars:
            print("No cars available.")
        for car in self.cars:
            print(car.get_details())


# 🧪 TEST CASES
if __name__ == "__main__":
    rental = CarRental("AutoGo", "Bulacan", "Eric")

    # Add cars
    car1 = ElectricCar("Tesla", "Model S", 2022, "Black", "E001", 1500, 100)
    car2 = GasCar("Toyota", "Altis", 2021, "White", "G001", 1000, "Gasoline")
    rental.add_car(car1)
    rental.add_car(car2)

    # Add customer
    cust1 = Customer("Mark", "C101")
    print(rental.add_customer(cust1))
    print(cust1.cash_in(2000))

    # Try renting
    print(rental.give_car(cust1, "E001", 1500))
    print(rental.give_car(cust1, "G999", 800))  # Invalid code

    # Display info
    print("\n--- Customers ---")
    rental.display_customers()

    print("\n--- Remaining Cars ---")
    rental.display_cars()

    # Return car
    print("\n--- Returning Car ---")
    print(cust1.return_car(car1, rental))
    rental.display_cars()
