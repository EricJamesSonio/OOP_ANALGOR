from inventory import Base, Inventory
from typing import List
from discount import Discount
import time


class Cashier:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class OrderItem:
    def __init__(self, item: Base):
        self.item = item
        self.price = item.price * self.quantity
        self.quantity = item.quantity
        self.name = item.name

    def get_details(self):
        return f"Name : {self.name}, Price : {self.price}, Quantity : {self.quantity}"


class Order:
    def __init__(self):
        self.orderitem: List["OrderItem"] = []
        self.date = time.strftime("%m/%d/%Y")
        self.time = time.strftime("%H/%M/%S")
        self.table_no = 0
        self.numguest = 0
        self.numitem = len(self.orderitem)

    def find_orderitem(self, code):
        for item in self.orderitem:
            if item.item.code == code:
                return item
        return None

    def add_orderitem(self, orderitem: OrderItem):
        item = self.find_orderitem(orderitem.item.code)
        if item:
            item.quantity += orderitem.item.quantity
        else:
            self.orderitem.append(orderitem)

    def display_orderitems(self):
        for order in self.orderitem:
            print(order.get_details())


class OrderProcessor:
    def __init__(self):
        self.orderhistory = []

    def calculate_total(self, order: Order):
        total = 0
        for item in order.orderitem:
            total += item.price
        return total

    def process_order(self, order: Order, discount: Discount, payment, cashier):
        total_price = self.calculate_total(order)
        discount_percent = discount.discount_percent()
        discounted_amount = discount_percent * total_price
        if discounted_amount <= payment:
            receipt = Receipt(
                order, total_price, discounted_amount, change, discount_percent
            )
            Receipt.receipt_counter += 1
            self.orderhistory.append(receipt)
            change = payment - discounted_amount
            return change


class Receipt:
    receipt_counter = 0

    def __init__(
        self, order: Order, total_price, discounted_amount, change, discount_percent
    ):
        self.order = order
        self.total_price = total_price
        self.discounted_price = discounted_amount
        self.discount_percent = discount_percent
        self.chagne = change
        self.receipt_no = Receipt.receipt_counter

    def generate(self):
        print("<-- Receipt -->")
        print(f"Date : {self.order.date}")
        print(f"Time : {self.order.time}")
        print(f"Receipt No : {self.receipt_no}")
        print(f"Item/s :")
        for item in self.order.orderitem:
            print(item.get_details())
        print(f"Total Price : {self.total_price}")
        print(f"Discount % : {self.discount_percent}")
        print(f"Total Payable : {self.discounted_price}")
        print(f"Change : {self.chagne}")
        print("Thankyou For buying!")
