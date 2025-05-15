from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime


class Product(ABC):
    def __init__(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_details(self):
        pass


class Appliances(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}"


class SchoolSupplies(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}"


class Inventory:
    def __init__(self):
        self.items: List[Product] = []
        self.observers: List["Observer"] = []

    def add_item(self, item: Product):
        for existing_item in self.items:
            if existing_item.code == item.code:
                existing_item.quantity += item.quantity
                self.notify(
                    {
                        "action": "add_stock",
                        "item": item,
                        "quantity": existing_item.quantity,
                    }
                )
                return

        self.items.append(item)
        self.notify({"action": "add_item", "item": item, "quantity": item.quantity})

    def find_item(self, code):
        for item in self.items:
            if item.code == code:
                return item
        return None

    def remove_item(self, code):
        item = self.find_item(code)
        if item:
            self.items.remove(item)
            self.notify(
                {"action": "removed_item", "item": item, "quantity": item.quantity}
            )
        else:
            return None

    def update_stock(self, code, quantity):
        item = self.find_item(code)
        if item:
            item.quantity += quantity
            self.notify(
                {"action": "update_stock", "item": item, "quantity": item.quantity}
            )
        else:
            return None

    def add_observer(self, observer: "Observer"):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


class InventoryViewer:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def display_inventory(self):
        for item in self.inventory.items:
            print(item.get_details())


class Observer(ABC):
    def __init__(self):
        self.records = []

    @abstractmethod
    def update(self, message):
        pass


class Logger(Observer):
    def __init__(self):
        super().__init__()

    def update(self, message):
        if message["action"] == "add_item":
            item = message["item"]
            quantity = message["quantity"]
            record = f"Added Item : {item} Quantity : {quantity} !"
            self.records.append(record)
        elif message["action"] == "removed_item":
            item = message["item"]
            quantity = message["quantity"]
            record = f"Removed Item : {item} Quantity : {quantity} !"
            self.records.append(record)
        else:
            return


class StockAlertSystem(Observer):
    def __init__(self):
        super().__init__()

    def update(self, message):
        if message["action"] == "add_stock":
            item = message["item"]
            quantity = message["quantity"]
            record = f"Added stock : {item} Quantity : {quantity} !"
            self.records.append(record)
        elif message["action"] == "update_stock":
            item = message["item"]
            quantity = message["quantity"]
            record = f"Update stock : {item} Quantity : {quantity} !"
            self.records.append(record)
        else:
            return


class RecordViewer:
    def __init__(self, observer: Observer):
        self.observer = observer

    def display_records(self):
        for record in self.observer.records:
            print(record)


class Store:
    def __init__(self, name, location, owner):
        self.name = name
        self.location = location
        self.owner = owner
        self.inventory = Inventory()
        self.logger = Logger()
        self.stockalertsystem = StockAlertSystem()
        self.inventoryviewer = InventoryViewer(self.inventory)

        self.inventory.add_observer(self.logger)
        self.inventory.add_observer(self.stockalertsystem)

    def add_item(self, item):
        self.inventory.add_item(item)

    def find_item(self, code):
        return self.inventory.find_item(code)

    def remove_item(self, code):
        self.inventory.remove_item(code)

    def display_inventory(self):
        self.inventoryviewer.display_inventory()


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass


class PWDDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.90


class SeniorDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.80


class BulkDiscount(DiscountStrategy):
    def apply_discount(self, price):
        if price > 100:
            return price * 0.90
        else:
            return price


class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price


class Cart:
    def __init__(self, store: Store, discount: DiscountStrategy):
        self.store = store
        self.discount = discount
        self.items: List["Product"] = []

    def add_to_cart(self, item: Product, quantity):
        product = self.store.find_item(item.code)
        if isinstance(product, Product) and product.quantity >= quantity:
            cart_item = type(product)(
                product.name, product.code, product.price, quantity
            )
            self.items.append(cart_item)
            self.store.inventory.update_stock(product.code, -quantity)
        else:
            return "Item doesn't exist"

    def update_cart_quantity(self, code, new_quantity):
        for item in self.items:
            if item.code == code:
                diff = item.quantity - new_quantity
                item.quantity = new_quantity
                self.store.inventory.update_stock(code, -diff)
                return
        return "Item doesn't exist"

    def remove_to_cart(self, code):
        for item in self.items:
            if item.code == code:
                self.store.inventory.update_stock(code, item.quantity)
                self.items.remove(item)
                return

    def display_cart(self):
        for item in self.items:
            print(item.get_details())


class Customer:
    def __init__(self, store: Store, discount: DiscountStrategy):
        self.cart = Cart(store, discount)


class OrderProcessor:
    def __init__(self, cart: Cart, discount_strategy: DiscountStrategy):
        self.cart = cart
        self.discount_strategy = discount_strategy

    def compute_subtotal(self):
        return sum(item.price * item.quantity for item in self.cart.items)

    def compute_total(self):
        subtotal = self.compute_subtotal()
        return self.discount_strategy.apply_discount(subtotal)

    def compute_tax(self, rate=0.12):
        return self.compute_total() * rate

    def final_total(self):
        return self.compute_total() + self.compute_tax()


class Receipt:

    receipt_no = 0

    def __init__(self, store: Store, cart: Cart, order_processor: OrderProcessor):
        self.store = store
        self.cart = cart
        self.order_processor = order_processor
        self.date_time = datetime.now()

        # Increment and assign unique receipt number
        Receipt.receipt_no += 1
        self.receipt_number = Receipt.receipt_no

    def generate_receipt(self):
        print("=" * 40)
        print(f"{self.store.name}")
        print(f"{self.store.location}")
        print(f"Owner: {self.store.owner}")
        print(f"Receipt No: {self.receipt_number}")
        print(f"Date: {self.date_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 40)
        print(f"{'Item':<15}{'Qty':<5}{'Price':<8}{'Total':<8}")
        print("-" * 40)

        for item in self.cart.items:
            name = item.name[:14]  # Truncate if too long
            qty = item.quantity
            price = item.price
            total = qty * price
            print(f"{name:<15}{qty:<5}{price:<8.2f}{total:<8.2f}")

        print("-" * 40)

        subtotal = self.order_processor.compute_subtotal()
        discounted_total = self.order_processor.compute_total()
        tax = self.order_processor.compute_tax()
        final_total = self.order_processor.final_total()
        discount_amount = subtotal - discounted_total

        print(f"{'Subtotal:':<30}{subtotal:.2f}")
        print(f"{'Discount:':<30}-{discount_amount:.2f}")
        print(f"{'Tax (12%):':<30}{tax:.2f}")
        print(f"{'Total Payable:':<30}{final_total:.2f}")
        print("=" * 40)
        print("Thank you for shopping with us!")
        print("=" * 40)
