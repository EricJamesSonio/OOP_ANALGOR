from inventory import *


class Store:
    def __init__(self):
        self.inventories = {
            "food": FoodMenuInventory(),
            "ingredients": IngredientInventory(),
        }
        self.current_inventory = None
        self.logger = Logger()
        self.stockalert = StockAlertSystem()

    def config_inventories(self):
        for inventory in self.inventories.values():
            inventory.add_observer(self.logger)
            inventory.add_observer(self.stockalert)

    def choose_inventory(self, inventory_type):
        if inventory_type in self.inventories:
            self.current_inventory = self.inventories[inventory_type]
        else:
            raise ValueError(f"Inventory Type Doesn't exist {inventory_type}")

    def raise_error(self):
        if self.current_inventory is None:
            raise ValueError("Choose Inventory First!")

    def raise_error_food(self):
        if not isinstance(self.current_inventory, FoodMenuInventory):
            raise ValueError("Not a Food Menu Inventory")

    def add_item(self, item):
        self.raise_error()
        self.current_inventory.add_item(item)

    def find_item(self, code):
        self.raise_error()
        self.current_inventory.find_item(code)

    def remove_item(self, code):
        self.raise_error()
        self.current_inventory.remove_item(code)

    def display_items(self):
        self.raise_error()
        self.current_inventory.display_items()

    def display_main_course(self):
        self.raise_error()
        self.raise_error_food()
        self.current_inventory.display_main_course()

    def display_dessert(self):
        self.raise_error()
        self.raise_error_food()
        self.current_inventory.display_dessert()
