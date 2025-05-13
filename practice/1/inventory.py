from product import *


class Inventory:
    def __init__(self):
        self.products: List[Product] = []
        self.observers: List[Observer] = []

    def add_item(self, item: Product):
        product = self.find_item(item.code)
        if product:
            product.quantity += item.quantity
            self.notify(
                {
                    "action": "add_stock",
                    "item": product,
                    "quantity": product.quantity,
                    "added": item.quantity,
                }
            )
        else:
            self.products.append(item)
            self.notify({"action": "new_item", "item": item, "quantity": item.quantity})

    def remove_item(self, code):
        product = self.find_item(code)
        if product:
            self.products.remove(product)
            self.notify(
                {
                    "action": "removed_item",
                    "item": product,
                    "quantity": product.quantity,
                }
            )
        else:
            return "Product Doesnt exist"

    def update_stock(self, code, quantity):
        product = self.find_item(code)
        if product and product.quantity > quantity:
            product.quantity -= quantity
            self.notify(
                {
                    "action": "removed_stock",
                    "item": product,
                    "quantity": product.quantity,
                    "removed": quantity,
                }
            )
        elif product and product.quantity == quantity:
            self.remove_item(product.code)
        else:
            return "Doesn't exist"

    def find_item(self, code):
        for existing_item in self.products:
            if existing_item.code == code:
                return existing_item

    def add_observer(self, observer: "Observer"):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


class InventoryViewer:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def display(self):
        for product in self.inventory.products:
            print(product.get_details())


class Observer(ABC):
    def __init__(self):
        self.records = []

    @abstractmethod
    def update(self, message):
        pass

    @abstractmethod
    def display_records(self):
        pass


class Logger(Observer):
    def __init__(self):
        super().__init__()

    def update(self, message):
        if message["action"] == "new_item":
            item = message["item"]
            quantity = message["quantity"]
            new = f"Added new Item! {item.name} Qtty : {quantity} !"
            return self.records.append(new)
        elif message["action"] == "removed_item":
            item = message["item"]
            quantity = message["quantity"]
            new = f"Removed item! Item : {item.name} Qtty : {quantity} !"
            return self.records.append(new)
        else:
            return

    def display_records(self):
        for record in self.records:
            print(record)


class StockAlertSystem(Observer):
    def __init__(self):
        super().__init__()

    def update(self, message):
        if message["action"] == "add_stock":
            item = message["item"]
            quantity = message["quantity"]
            new = f"Added Stock For ! {item.name} + Qtty : {quantity} !"
            return self.records.append(new)
        elif message["action"] == "removed_stock":
            item = message["item"]
            quantity = message["quantity"]
            new = f"Reduced Stock For ! {item.name} - Qtty : {quantity} !"
            return self.records.append(new)
        else:
            return

    def display_records(self):
        for record in self.records:
            print(record)
