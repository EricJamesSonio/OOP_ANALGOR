from product import *


class Inventory:
    def __init__(self):
        self.items: List["Product"] = []
        self.observer: List["Observer"] = []

    def find_item(self, code):
        for existing_item in self.items:
            if existing_item.code == code:
                return existing_item
        return None

    def add_item(self, item: Product):
        product = self.find_item(item.code)
        if product:
            product.quantity += item.quantity
            self.notify({"act": "add_stock", "item": item, "quantity": item.quantity})
        else:
            self.items.append(item)
            self.notify({"act": "add_item", "item": item, "quantity": item.quantity})

    def remove_item(self, code):
        product = self.find_item(code)
        if product:
            self.items.remove(product)
            self.notify(
                {"act": "removed", "item": product, "quantity": product.quantity}
            )
        else:
            return "Doesn't Exist"
        
    def update_stock(self, item, quantity: int):
        product = self.find_item(item.code)
        if product:
            product.update_stock(quantity)
        else:
            print(f"Product {item.name} not found.")

    def add_observer(self, observer: "Observer"):
        self.observer.append(observer)

    def notify(self, message):
        for observer in self.observer:
            observer.update(message)

class InventoryViewer:
    def __init__(self, inventory : Inventory):
        self.inventory = inventory
        
    def display(self):
        for items in self.inventory.items:
            print(items.get_details())

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class Manager(Observer):
    def __init__(self):
        self.updates = []

    def update(self, message):
        if message["act"] == "add_item":
            item = message["item"]
            quantity = message["quantity"]
            new = f"New item : {item.name} Added! with Qtty of : {quantity}"
            self.updates.append(new)
        elif message["act"] == "add_stock":
            item = message["item"]
            quantity = message["quantity"]
            new = f"Added stock! : {item.name} Added! with Qtty of : {quantity}"
            self.updates.append(new)
        elif message["act"] == "removed":
            item = message["item"]
            quantity = message["quantity"]
            new = f"Removed : {item.name} ! with Qtty of : {quantity}"
            self.updates.append(new)

    def display(self):
        for update in self.updates:
            print(update)


#### Tester!
# Create product instances (ensure these are defined in your product module)
item1 = DigitalProduct("E-Book", "D001", 10.0, 50, "2025-12-31", "N/A")
item2 = PhysicalProduct("Laptop", "P001", 1000.0, 30, "2026-01-01", "15-inch")

# Initialize Inventory and Manager (Observer)
inventory = Inventory()
manager = Manager()

# Add observer to inventory
inventory.add_observer(manager)

# Add products to inventory
inventory.add_item(item1)
inventory.add_item(item2)
inventory.add_item(item2)

# Remove a product from inventory
inventory.remove_item("D001")

# Display updates for the manager
manager.display()
