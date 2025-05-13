from inventory import *

class Store:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Store, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, name, location, owner):
        if self._initialized:
            return
        self.inventory = Inventory()
        self.logger = Logger()
        self.stock_alert = StockAlertSystem()
        self.inventory.add_observer(self.logger)
        self.inventory.add_observer(self.stock_alert)
        self._initialized = True
        self.inventoryviewer = InventoryViewer(self.inventory)
        self.name = name
        self.location = location
        self.owner = owner
        self.description = None

    def add_item(self, item):
        self.inventory.add_item(item)
        
    def remove_item(self, code):
        self.inventory.remove_item(code)
        
    def update_stock(self, code, quantity):
        self.inventory.update_stock(code, quantity)
        
    def find_item(self, code):
        return self.inventory.find_item(code)
        
    def display_inventory(self):
        self.inventoryviewer.display()
        
    def view_logs(self):
        self.logger.display_records()
        
    def view_stockAlert(self):
        self.stock_alert.display_records()
        
    def clear_logs(self):
        self.logger.records.clear()
        
    def edit_description(self):
        print("< -- Edit Description -- >")
        description = input("Enter here : ")
        self.description = description
        return True
        
class StoreInfo:
    def __init__(self, store : Store):
        self.store = store
        
    def display_info(self):
        print("< -- Store Info ==>")
        print(f"Name : {self.store.name}")
        print(f"Location : {self.store.location}")
        print(f"Owner : {self.store.owner}")
        print(f"Description : {self.description}")
        
        
        

