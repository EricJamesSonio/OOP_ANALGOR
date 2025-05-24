from abc import ABC, abstractmethod
from typing import List


class Product:
    def __init__(self, name, code, sales_price, cost_price, quantity):
        self.name = name
        self.id = code
        self.cost_price = cost_price
        self.sales_price = sales_price
        self.quantity = quantity

    def get_details(self):
        return f"Name : {self.name}, Id : {self.id}, Price : {self.sales_price}, Quantity : {self.quantity}"

    def __str__(self):
        return self.name


# ------------ Main Course ------------ #


class Food(Product):
    pass


class MainCourse(Food):
    pass


class FriedChicken(MainCourse):
    pass


class PorkBarbeque(MainCourse):
    pass


# ------------ Side Dish ------------ #


class SideDish(Food):
    pass


class Cream(SideDish):
    pass


class Vegetable(SideDish):
    pass
