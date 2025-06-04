from abc import ABC, abstractmethod
from typing import List, Optional

# ----------- Product Item (Base Form) -------------- #


class ProductItem:
    def __init__(self, name, id, size, price, quantity):
        self.name = name
        self.id = id
        self.size = size
        self.price = price
        self.quantity = quantity

    def get_details(self):
        return f"Name : {self.name}, Id : {self.id}, Size : {self.size}, Price : {self.price}, Quantity : {self.quantity}"


# ----------- Main Course -------------- #


class MainCourse(ProductItem):
    pass


class ChickenJoy(MainCourse):
    pass


class Spaghetti(MainCourse):
    pass


# ----------- Side Dish -------------- #


class SideDish(ProductItem):
    pass


class Pizza(SideDish):
    pass


class PineApplePizza(Pizza):
    pass


class CheesePizza(Pizza):
    pass


# ----------- Users -------------- #


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"Name : {self.name} , Id : {self.id}"


class Customer(User):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.registered = False


class Employee(User, ABC):
    def __init__(self, name, id, store="Store"):
        super().__init__(name, id)
        self.store = store

    @abstractmethod
    def get_details(self):
        pass


class Cashier(Employee):
    _cashier_counter = 0

    def __init__(self, name, id, store="Store"):
        super().__init__(name, id, store)
        self.cashier_no = Cashier._cashier_counter
        Cashier._cashier_counter += 1

    def get_details(self):
        return f" [{self.cashier_no}]. Name : {self.name}, Id : {self.id} , Store : {self.store}"


class Manager(Employee):
    _manager_counter = 0

    def __init__(self, name, id, store="Store"):
        super().__init__(name, id, store)
        self.manager_no = Manager._manager_counter
        Manager._manager_counter += 1

    def get_details(self):
        return f" [{self.manager_no}]. Name : {self.name}, Id : {self.id} , Store : {self.store}"


# ----------- Inventory -------------- #


class Inventory:
    def __init__(self):
        self.items: List[ProductItem] = []
        self.threshold = 10
        self.logger = Logger()
        self.stockalertsystem = StockAlertSystem()
        self.observers: List[Observer] = [self.logger, self.stockalertsystem]
        self.observerviewer = ObserverViewer()
        self.inventoryviewer = InventoryViewer(self)

    def find_item(self, id):
        for item in self.items:
            if item.id == id:
                return item
        return None

    def add_item(self, item):
        product = self.find_item(item.id)
        if product:
            product.quantity += item.quantity
        else:
            self.items.append(item)

    def remove_item(self, id):
        product = self.find_item(id)
        if product:
            self.items.remove(product)
        else:
            return None

    def reduce_stock(self, id, quantity):
        product = self.find_item(id)
        if product and quantity > 0:
            product.quantity -= quantity
            if product.quantity <= 0:
                self.items.remove(product)
            else:
                return "Successfully Reduce Stock"
        else:
            return "Quantity is Zero or below or Item Doesnt Exist"

        self.check_all_stock()

    def increase_stock(self, id, quantity):
        product = self.find_item(id)
        if product and quantity > 0:
            product.quantity += quantity
        else:
            return "Quantity is Zero or below or Item Doesnt Exist"

    def set_threshold(self, new_threshold):
        self.threshold = new_threshold

    def is_low_stock(self, id):
        product = self.find_item(id)
        if product.quantity <= self.threshold:
            self.notify("any")
            return True
        else:
            return False

    def check_all_stock(self):
        for item in self.items:
            true = self.is_low_stock(item.id)
            if true:
                self.notify("Any")

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def display_logger(self):
        self.observerviewer.display_records(self.logger)

    def display_stockalertsystem(self):
        self.observerviewer.display_records(self.stockalertsystem)

    def display_all_records(self):
        self.display_logger()
        self.display_stockalertsystem

    def display_items(self):
        self.inventoryviewer.display_items()


class InventoryViewer:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def display_items(self):
        for item in self.inventory.items:
            print(item.get_details())


# ----------- Observer -------------- #


class Observer(ABC):
    def __init__(self):
        self.records = []

    @abstractmethod
    def update(self, message):
        pass


class Logger(Observer):
    pass


class StockAlertSystem(Observer):
    pass


class ObserverViewer:
    def __init__(self):
        pass

    def display_records(self, observer: Observer):
        for record in observer.records:
            print(record)


# ----------- Store -------------- #


class Store:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.inventory = Inventory()

    def add_item(self, item):
        self.inventory.add_item(item)

    def find_item(self, id):
        self.inventory.find_item(id)

    def remove_item(self, id):
        self.inventory.remove_item(id)

    def reduce_stock(self, id, quantity):
        self.inventory.reduce_stock(id, quantity)

    def increase_stock(self, id, quantity):
        self.inventory.increase_stock(id, quantity)

    def set_threshold(self, new_threshold):
        self.inventory.set_threshold(new_threshold)

    def display_items(self):
        self.inventory.display_items()

    def display_logger(self):
        self.inventory.display_logger()

    def display_stockalertsystem(self):
        self.inventory.display_stockalertsystem()

    def display_all_records(self):
        self.inventory.display_all_records()


# ----------- Employee Management -------------- #


class EmployeeManagement:
    def __init__(self, store: Store):
        self.store = store
        self.employees: List[Employee] = []
        self.empviewer = EmployeeViewer(self)

    def find_emp(self, id):
        for emp in self.employees:
            if emp.id == id:
                return emp
        return None

    def add_item(self, emp):
        existing_emp = self.find_emp(emp.id)
        if existing_emp:
            return "Already In"
        else:
            self.employees.append(emp)

    def remove_emp(self, id):
        product = self.find_emp(id)
        if product:
            self.employees.remove(product)
        else:
            return None

    def display_emp(self):
        self.empviewer.display_emp()

    def modify_emp(self, id):
        print("Modify Employees")
        self.display_emp()
        choice = int(input("Type Emp Id : "))
        emp = self.find_emp(choice)
        if emp:
            print(emp.get_details())
            print("[1]. Name")
            print("[2]]. Id")
            choice2 = int(input("Enter : "))
            if choice2 == 1:
                name = str(input("Enter New Name : "))
                emp.name = name
            elif choice2 == 2:
                id = int(input("Enter Id : "))
                emp.id = id
            else:
                return
            return None


class EmployeeViewer:
    def __init__(self, employeemanagement: EmployeeManagement):
        self.employeemanagement = employeemanagement

    def display_emp(self):
        for emp in self.employeemanagement.employees:
            print(emp.get_details())
