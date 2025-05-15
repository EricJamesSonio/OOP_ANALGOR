from cart import *
from orderprocessor import *


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def shop(self, product, quantity):
        self.cart.add_to_cart(product, quantity)

    def checkout(self, discount, payment_method):
        processor = OrderProcessor(discount, payment_method)
        processor.process(self.cart)
