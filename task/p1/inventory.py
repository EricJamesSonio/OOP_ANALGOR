from typing import List
from abc import ABC, abstractmethod


class Product:
    def __init__(self, name, code, quantity, price):
        self.name = name
        self.code = code
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Name : {self.name}, Code : {self.code}, Quantity : {self.quantity}, Price : {self.price}"

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def get_quantiy(self):
        return self.quantity

    def get_price(self):
        return self.price


class DiscountStrategy(ABC):
    def __init__(self):
        self.discount = None

    @abstractmethod
    def apply_discount(self, price):
        pass


class PWDDiscount(DiscountStrategy):
    def __init__(self):
        self.discount = 0.90

    def apply_discount(self, price):
        return price * self.discount


class SeniorDiscount(DiscountStrategy):
    def __init__(self):
        super().__init__()
        self.discount = 0.85

    def apply_discount(self, price):
        return price * self.discount


class OrderItem:
    def __init__(self, product: Product):
        self.product = product
        self.name = product.name
        self.price = product.price
        self.date = None


class Order:
    def __init__(self, discount: DiscountStrategy):
        self.order_items: List[OrderItem] = []
        self.discount = discount

    def add_orderitem(self, orderitem: OrderItem):
        self.order_items.append(orderitem)

    def total_price(self) -> float:
        total = 0
        for order in self.order_items:
            order.price += total
        return total

    def discounted_price(self):
        price = self.total_price()
        discounted = self.discount.apply_discount(price)
        return discounted

    def pay(self, pay):
        total_payable = self.discounted_price()
        pay_amount = pay
        change = total_payable - pay_amount
        if change >= 0:
            return change
        else:
            return "Insufficient Amount"


class Customer:
    def __init__(self, name, id, age, pwd: bool):
        self.name = name
        self.id = id
        self.age = age
        self.pwd = pwd
        self.discount: List[DiscountStrategy] = []

    def __str__(self):
        return f"Name : {self.name}, Id : {self.id}, Age : {self.age}, Pwd : {self.pwd},Discount : {self.discount}"


""" # i remove this since i want to have stack of discount but if i dont want stacking ill keep this then recode the membership factory   
class PWDCustomer(Customer):
    def __init__(self, name, id, age, pwd):
        super().__init__(name, id, age, pwd)
        self.discount = PWDDiscount()
        
class SeniorCustomer(Customer):
    def __init__(self, name, id, age, pwd):
        super().__init__(name, id, age, pwd)
        self.discount = SeniorDiscount()
        """


class MemberShipFactory:
    def create(self, customer: Customer):
        if customer.age >= 60:
            customer.discount.append(SeniorDiscount())
        if customer.pwd:
            customer.discount.append(PWDDiscount())


class Cashier:
    def __init__(self, id, balance, paid, income, profit):
        self.id = id
        self.balance = balance
        self.income = income
        self.paid = paid
        self.profit = profit

    def process_order(self):
        pass


class Inventory:
    def __init__(self):
        self.items: List[Product] = []

    def find_item(self, code):
        for item in self.items:
            if item.code == code:
                return item
        return None

    def add_item(self, item):
        product = self.find_item(item.code)
        if product:
            product.quantity += item.quantity
        else:
            self.items.append(item)

    def incrementquantity(self, code):
        product = self.find_item(code)
        if product:
            product.quantity += 1
        else:
            return None

    def decrementquantity(self, code):
        product = self.find_item(code)
        if product:
            product.quantity -= 1
        else:
            return None

    def display(self):
        for item in self.items:
            print(item)
