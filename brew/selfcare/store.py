from inventory import *

class Store:
    def __init__(self):
        self.inventory = Inventory()
        self.inventoryviewer = InventoryViewer(self.inventory)
        self.logger = Logger()
        self.stockalert = StockAlertSystem()
        self.inventory.add_observer(self.logger)
        self.inventory.add_observer(self.stockalert)
        self.loggerviewer = ObserverViewer(self.logger)
        self.stockalertviewer = ObserverViewer(self.stockalert)
        
    def add_item(self, item):
        self.inventory.add_item(item)
        
    def find_item(self, code):
        return self.inventory.find_item(code)
        
    def remove_item(self,code):
        self.inventory.remove_item(code)
        
    def display_items(self):
        self.inventory.display_items()
        
    def update_stock(self, code, quantity):
        self.inventory.update_stock(code, quantity)
        
    def display_logger(self):
        self.loggerviewer.display_records()
        
    def display_stock(self):
        self.stockalertviewer.display_records() 
        

        

        
        