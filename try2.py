from abc import ABC, abstractmethod
import time


# Abstract Observer
class StockObserver(ABC):
    @abstractmethod
    def update(self, item_name, stock_level, threshold):
        pass


# Subject (Observable)
class Inventory:
    def __init__(self):
        self.stock = {}
        self.observers = []

    def register_observer(self, observer: StockObserver):
        self.observers.append(observer)

    def remove_observer(self, observer: StockObserver):
        self.observers.remove(observer)

    def notify_observers(self, item_name, stock_level, threshold):
        for observer in self.observers:
            observer.update(item_name, stock_level, threshold)

    def update_stock(self, item_name, quantity, threshold):
        if item_name in self.stock:
            self.stock[item_name] -= quantity
            print(f"Updated stock for {item_name}: {self.stock[item_name]} remaining.")
        else:
            self.stock[item_name] = 0
            print(f"Item {item_name} not found, setting stock to 0.")

        # Check if stock is below threshold and notify
        if self.stock[item_name] < threshold:
            print(f"Stock for {item_name} is low! (Threshold: {threshold})")
            self.notify_observers(item_name, self.stock[item_name], threshold)
        else:
            print(f"Stock for {item_name} is sufficient: {self.stock[item_name]}")

    def add_item(self, item_name, quantity):
        self.stock[item_name] = self.stock.get(item_name, 0) + quantity
        print(f"Added {quantity} units of {item_name}.")


# Concrete Observers
class InventoryManager(StockObserver):
    def update(self, item_name, stock_level, threshold):
        print(
            f"[InventoryManager] Notified: Stock for {item_name} is below threshold. Restocking..."
        )
        restock_quantity = threshold * 2  # Restock double the threshold
        print(f"Restocking {item_name} by {restock_quantity} units.\n")
        Inventory.add_item(item_name, restock_quantity)


class Purchaser(StockObserver):
    def update(self, item_name, stock_level, threshold):
        print(f"[Purchaser] Notified: Stock for {item_name} is low. Ordering more...\n")
        self.order(item_name, threshold)

    def order(self, item_name, threshold):
        print(f"[Purchaser] Ordering more {item_name} to meet the threshold.\n")
        Inventory.add_item(item_name, threshold * 3)  # Ordering 3 times the threshold


class AlertSystem(StockObserver):
    def update(self, item_name, stock_level, threshold):
        print(f"[AlertSystem] ALERT: {item_name} stock is below the threshold!\n")
        print(f"Stock level: {stock_level}, Threshold: {threshold}\n")


# Simulating the system
def simulate_inventory_system():
    # Set up inventory and observers
    inventory = Inventory()
    inventory.register_observer(InventoryManager())
    inventory.register_observer(Purchaser())
    inventory.register_observer(AlertSystem())

    # Add some initial stock
    inventory.add_item("Garlic", 100)
    inventory.add_item("Chicken", 50)

    # Update stock and simulate running out
    time.sleep(1)  # Adding a small delay for the simulation
    inventory.update_stock("Garlic", 95, 10)  # Garlic stock drops below 10
    inventory.update_stock("Chicken", 45, 10)  # Chicken stock drops below 10

    # Further updates and low stock alerts
    time.sleep(1)
    inventory.update_stock("Garlic", 10, 10)  # Garlic stock reaches the threshold
    inventory.update_stock("Chicken", 5, 10)  # Chicken stock reaches the threshold


# Run the simulation
simulate_inventory_system()
