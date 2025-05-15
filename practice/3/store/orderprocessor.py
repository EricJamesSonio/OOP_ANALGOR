from receipt import *


class OrderProcessor:
    def __init__(self, discount_strategy, payment_strategy):
        self.discount = discount_strategy
        self.payment = payment_strategy
        self.receipt = Receipt()

    def process(self, cart):
        subtotal = sum(item.price * item.quantity for item in cart.items)
        discounted = self.discount.apply(subtotal)
        final_amount = self.payment.process_payment(discounted)
        self.receipt.generate(cart.items, final_amount, self.payment.__class__.__name__)
