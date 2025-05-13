from inventory import *


class StoreConfiguration:
    def __init__(self):
        # Using Singleton instance of Store
        self.store = Store.get_instance("7/11", "Bagong Barrio", "Eric James")
        self.store.inventory.add_observer(self.store.logger)
        self.store.inventory.add_observer(self.store.stockalert)


class Store:
    _instance = None  # Class-level variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        # If instance does not exist, create one
        if cls._instance is None:
            cls._instance = super(Store, cls).__new__(cls)
        return cls._instance

    def __init__(self, name, location, owner):
        if not hasattr(
            self, "initialized"
        ):  # Check to ensure the object is initialized once
            self.name = name
            self.location = location
            self.owner = owner
            self.inventory = Inventory()
            self.logger = Logger()
            self.stockalert = StockAlert()
            self.inventoryviewer = InventoryViewer(self.inventory)
            self.initialized = True  # Mark as initialized

    @classmethod
    def get_instance(cls, name, location, owner):
        return cls(name, location, owner)  # Return the Singleton instance

    def add_item(self, item):
        self.inventory.add_item(item)

    def find_item(self, code):
        self.inventory.find_item(code)

    def remove_item(self, code):
        self.inventory.remove_item(code)

    def display_inventory(self):
        self.inventoryviewer.display()

    def update_stock(self, code):
        self.inventory.update_stock(code)
