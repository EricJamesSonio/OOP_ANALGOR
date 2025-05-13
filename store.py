from abc import ABC, abstractmethod
from typing import List, Optional


class Product(ABC):
    def __init__(self, name, id, price, quantity):
        self.name = name
        self.id = id
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_details(self):
        pass


class Electronic(Product):
    def __init__(self, name, id, price, quantity):
        super().__init__(name, id, price, quantity)

    def get_details(self):
        return f"Name : {self.name}, Id : {self.id}, Price : {self.price}, Quantity : {self.quantity}"


class Clothing(Product):
    def __init__(self, name, id, price, quantity):
        super().__init__(name, id, price, quantity)

    def get_details(self):
        return f"Name : {self.name}, Id : {self.id}, Price : {self.price}, Quantity : {self.quantity}"


class Book(Product):
    def __init__(self, name, id, price, quantity):
        super().__init__(name, id, price, quantity)

    def get_details(self):
        return f"Name : {self.name}, Id : {self.id}, Price : {self.price}, Quantity : {self.quantity}"


class Helper:
    @staticmethod
    def helper_function():
        name = input("Name : ")
        id = int(input("Id : "))
        price = float(input("Price : "))
        quantity = int(input("Quantity : "))
        return name, id, price, quantity


class Factory:

    def create(self, product_type: str):
        if product_type == "Electronic":
            name, id, price, quantity = Helper.helper_function()
            return Electronic(name, id, price, quantity)

        elif product_type == "Book":
            name, id, price, quantity = Helper.helper_function()
            return Book(name, id, price, quantity)

        elif product_type == "Clothing":
            name, id, price, quantity = Helper.helper_function()
            return Clothing(name, id, price, quantity)


class Printer:
    @staticmethod
    def print_message(message):
        print(message)


class InputClass:
    def __init__(self):
        self.factory = Factory()

    def creating_product(self):
        print("<-- Product Type -->")
        print("[1]. Book")
        print("[2]. Clothing")
        print("[3]. Electronic")
        choice = input("Enter Choice : ")
        if choice == "1":
            Printer.print_message("Create Book Product")
            book = self.factory.create("Book")
            return Printer.print_message(book.get_details())
        elif choice == "2":
            Printer.print_message("Create Clothing Product")
            clothing = self.factory.create("Clothing")
            return Printer.print_message(clothing.get_details())
        elif choice == "3":
            Printer.print_message("Create Electronic Product")
            electronic = self.factory.create("Electronic")
            return Printer.print_message(electronic.get_details())
        else:
            Printer.print_message("Choice invalid")
            return
