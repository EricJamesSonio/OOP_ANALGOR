from abc import ABC, abstractmethod
from datetime import datetime


class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Item:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity


class Cart:
    def __init__(self, store, discount_strategy):
        self.store = store
        self.items = []
        self.undo_stack = []
        self.discount_strategy = discount_strategy

    def add_item(self, item):
        self.items.append(item)
        self.undo_stack.append(("add", item))

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                self.undo_stack.append(("remove", item))
                break

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        action, item = self.undo_stack.pop()
        if action == "add":
            self.items.remove(item)
        elif action == "remove":
            self.items.append(item)

    def clear_cart(self):
        self.items.clear()
        self.undo_stack.clear()


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, subtotal):
        pass


class NoDiscount(DiscountStrategy):
    def apply_discount(self, subtotal):
        return subtotal


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent):
        self.percent = percent

    def apply_discount(self, subtotal):
        return subtotal * (1 - self.percent / 100)


class OrderProcessor:
    def __init__(self, cart, discount_strategy, tax_rate=0.12):
        self.cart = cart
        self.discount_strategy = discount_strategy
        self.tax_rate = tax_rate

    def subtotal(self):
        return sum(item.price * item.quantity for item in self.cart.items)

    def discount_amount(self):
        subtotal = self.subtotal()
        return subtotal - self.discount_strategy.apply_discount(subtotal)

    def discounted_total(self):
        return self.discount_strategy.apply_discount(self.subtotal())

    def tax_amount(self):
        return self.discounted_total() * self.tax_rate

    def final_total(self):
        return self.discounted_total() + self.tax_amount()


class Receipt:
    def __init__(self, store, cart, order_processor):
        self.store = store
        self.cart = cart
        self.processor = order_processor
        self.date = datetime.now()

    def generate_receipt(self):
        print("\n" + "=" * 40)
        print(f"{self.store.name:^40}")
        print(f"{self.store.address:^40}")
        print(f"{'RECEIPT':^40}")
        print(f"{self.date.strftime('%Y-%m-%d %H:%M:%S'):^40}")
        print("=" * 40)
        print(f"{'ITEM':<20}{'QTY':>5}{'PRICE':>7}{'TOTAL':>8}")
        print("-" * 40)
        for item in self.cart.items:
            total_price = item.price * item.quantity
            print(
                f"{item.name:<20}{item.quantity:>5}{item.price:>7.2f}{total_price:>8.2f}"
            )
        print("-" * 40)
        print(f"{'SUBTOTAL:':<32}{self.processor.subtotal():>8.2f}")
        print(f"{'DISCOUNT:':<32}{self.processor.discount_amount():>8.2f}")
        print(f"{'TAX:':<32}{self.processor.tax_amount():>8.2f}")
        print(f"{'TOTAL:':<32}{self.processor.final_total():>8.2f}")
        print("=" * 40)


class Customer:
    def __init__(self, name, store, discount_strategy):
        self.name = name
        self.cart = Cart(store, discount_strategy)
        self.order_history = []

    def add_to_cart(self, item):
        self.cart.add_item(item)

    def remove_from_cart(self, item_name):
        self.cart.remove_item(item_name)

    def undo_last_action(self):
        self.cart.undo()

    def checkout(self, payment_amount):
        if not self.cart.items:
            print("Cart is empty. Cannot checkout.")
            return

        processor = OrderProcessor(self.cart, self.cart.discount_strategy)
        total = processor.final_total()

        if payment_amount < total:
            print(
                f"Insufficient payment. Total is {total:.2f}, but paid {payment_amount:.2f}."
            )
            return

        change = round(payment_amount - total, 2)
        receipt = Receipt(self.cart.store, self.cart, processor)
        self.order_history.append(receipt)
        receipt.generate_receipt()
        print(f"Payment successful. Change: ₱{change:.2f}")
        self.cart.clear_cart()
