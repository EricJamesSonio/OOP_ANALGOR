from abc import ABC, abstractmethod
from typing import List

# ------------------ Desk ------------------ #

class Desk(ABC):
    def __init__(self, code: str, price: float):
        self.code = code
        self.price = price


class Hotdesk(Desk):
    def __init__(self, code: str):
        super().__init__(code, 100)


class DedicatedDesk(Desk):
    def __init__(self, code: str):
        super().__init__(code, 200)


class PrivateOffice(Desk):
    def __init__(self, code: str):
        super().__init__(code, 500)


# ------------------ Discount Strategy ------------------ #

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass


class RegularDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price


class StartUpDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.90


class EnterpriseUserDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.80


# ------------------ Payment ------------------ #

class Payment:
    def __init__(self, customer: 'User'):
        self.customer = customer

    def pay(self, amount: float, price_to_pay: float) -> float:
        discounted_price = self.customer.discount.apply_discount(price_to_pay)
        return discounted_price - amount


# ------------------ Wallet ------------------ #

class Wallet:
    def __init__(self, user: 'User'):
        self.user = user
        self.balance = 0.0

    def cash_in(self, amount: float):
        if amount > 0:
            self.balance += amount


# ------------------ Observer ------------------ #

class Observer(ABC):
    def __init__(self):
        self.records = []

    @abstractmethod
    def update(self, message: dict):
        pass


class Logger(Observer):
    def update(self, message: dict):
        item = message.get("item")
        if message["action"] == "add_item":
            self.records.append(f"Added Item: {item.code} to inventory")
        elif message["action"] == "removed_item":
            self.records.append(f"Removed Item: {item.code} from inventory")


class Email(Observer):
    def update(self, message: dict):
        if message["action"] == "bought":
            item, price = message["item"], message["price"]
            self.records.append(f"Bought Desk: {item.code}, Price: {price}")


class SMS(Email):
    pass


class InApp(Email):
    pass


class RecordViewer:
    def __init__(self, observer: Observer):
        self.observer = observer

    def display_records(self):
        for record in self.observer.records:
            print(record)


# ------------------ Inventory ------------------ #

class Inventory:
    def __init__(self):
        self.items: List[Desk] = []
        self.observers: List[Observer] = []

    def find_item(self, code: str):
        return next((item for item in self.items if item.code == code), None)

    def add_item(self, desk: Desk):
        if not self.find_item(desk.code):
            self.items.append(desk)
            self.notify({"action": "add_item", "item": desk})

    def remove_item(self, code: str):
        item = self.find_item(code)
        if item:
            self.items.remove(item)
            self.notify({"action": "removed_item", "item": item})

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify(self, message: dict):
        for observer in self.observers:
            observer.update(message)


class InventoryViewer:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def display_inventory(self):
        for item in self.inventory.items:
            print(f"Desk Code: {item.code}, Price: {item.price}")


# ------------------ BookingWorkspace ------------------ #

class BookingWorkspace:
    def __init__(self):
        self.inventory = Inventory()
        self.inventory_viewer = InventoryViewer(self.inventory)
        self.logger = Logger()
        self.inventory.add_observer(self.logger)
        self.record_viewer = RecordViewer(self.logger)

    def add_item(self, desk: Desk):
        self.inventory.add_item(desk)

    def find_item(self, code: str):
        return self.inventory.find_item(code)

    def remove_item(self, code: str):
        self.inventory.remove_item(code)

    def give_desk(self, item: Desk, hours: int) -> float:
        desk = self.inventory.find_item(item.code)
        return desk.price * hours if desk else 0.0

    def display_inventory(self):
        self.inventory_viewer.display_inventory()

    def display_records(self):
        self.record_viewer.display_records()


# ------------------ Renting ------------------ #

class Renting:
    def __init__(self, user: 'User', workspace: BookingWorkspace):
        self.user = user
        self.workspace = workspace
        self.observers: List[Observer] = []

    def bought_desk(self, item: Desk, amount: float, hours: int):
        price = self.workspace.give_desk(item, hours)
        remaining = self.user.pay(amount, price)
        if remaining >= 0:
            self.user.desk.append(item)
            self.notify({"action": "bought", "item": item, "price": price})

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify(self, message: dict):
        for observer in self.observers:
            observer.update(message)


# ------------------ User ------------------ #

class User:
    def __init__(self, name: str, email: str, sms: str, discount: DiscountStrategy, payment: Payment, store: BookingWorkspace):
        self.name = name
        self.email = email
        self.sms = sms
        self.discount = discount
        self.payment = payment
        self.store = store
        self.wallet = Wallet(self)
        self.cart = Renting(self, store)
        self.desk: List[Desk] = []

    def pay(self, amount: float, price_to_pay: float) -> float:
        return self.payment.pay(amount, price_to_pay)

    def cash_in(self, amount: float):
        self.wallet.cash_in(amount)

    def rent_desk(self, item: Desk, amount: float, hours: int):
        self.cart.bought_desk(item, amount, hours)
        
