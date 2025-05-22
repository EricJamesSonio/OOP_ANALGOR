from products import Product, List
from discount import Discount
import time


class OrderItem:
    def __init__(self, product: Product):
        self.product = product
        self.price = self.product.price
        self.quantity = self.product.quantity

    def __str__(self):
        return


class Order:
    def __init__(self):
        self.orderitem: List[OrderItem] = []
        self.date = time.strftime("%m/%d/%Y")
        self.time = time.strftime("%H/%M/%S")
        self.table_no = 0
        self.numguest = 0
        self.numitems = len(self.orderitem)

    def add_order(self, orderitem: OrderItem):
        self.orderitem.append(orderitem)

    def total_price(self):
        total = 0
        for order in self.orderitem:
            order.price += total

        return total


class Cashier:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class OrderProcessor:
    def __init__(self):
        pass

    def process_order(self, order: Order, discount: Discount):
        total = order.total_price()
        discount = discount.percent_discount()
