from inventory import *
from baseproduct import ProductBase


class Store:
    def __init__(self):
        self.inventories = {
            "food": FoodMenuInventory(),
            "beverage": BeverageInventory(),
            "ingredient": IngredientInventory(),
        }

        self.logger = Logger()
        self.stockalert = StockAlertSystem()
        self.current_inventory = None

        for key in self.inventories:
            self.inventories[key].add_observer(self.logger)
            self.inventories[key].add_observer(self.stockalert)

    def set_inventory(self, inventory_type):
        if inventory_type not in self.inventories:
            raise ValueError(f"Inventory item doesn't exist: {inventory_type}")
        self.current_inventory = self.inventories[inventory_type]

    def error(self):
        if not self.current_inventory:
            raise RuntimeError("No inventory selected. Call set_inventory() first.")

    def add_item(self, item):
        self.error()
        self.current_inventory.add_item(item)

    def find_item(self, code):
        self.error()
        return self.current_inventory.find_item(code)

    def remove_item(self, code):
        self.error()
        self.current_inventory.remove_item(code)

    def update_stock(self, code, quantity):
        self.error()
        self.current_inventory.update_stock(code, quantity)

    def set_threshold(self, threshold):
        self.current_inventory.set_threshold(threshold)

    def display_inventory(self):
        self.error()
        InventoryViewer(self.current_inventory).display_inventory()


# Instantiate store and add item
store = Store()

item = ProductBase(
    name="Chicken Wings",
    code="CW001",
    price=120.0,
    supplier="Supplier A",
    quantity=10,
    unit="pcs",
    expiration_date="2025-12-31",
)

store.set_inventory("food")
store.add_item(item)
store.display_inventory()
