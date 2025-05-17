from product import *
from observer import *

class Inventory:
    def __init__(self):
        self.items : List[Product] = []
        self.observers : List[Observer] = []
        self.inventoryviewer = InventoryViewer(self)
        
    def find_item(self, code):
        for item in self.items:
            if item.code == code:
                return item
        return None
    
    def add_item(self, item : Product):
        product = self.find_item(item.code)
        if product:
            product.quantity += item.quantity
            self.notify({"action" : "add_stock" , "item" : product, "quantity" : item.quantity, "total" : product.quantity})
        else:
            self.items.append(item)
            self.notify({"action" : "add_item" , "item" : item, "quantity" : item.quantity})
            
    def remove_item(self, code):
        product = self.find_item(code)
        if product:
            self.items.remove(product)
            self.notify({"action" : "removed_item" , "item" : product, "quantity" : product.quantity})
        else:
            return None
        
    def update_stock(self, code, quantity):
        product = self.find_item(code)
        if product:
            product.quantity += quantity
            self.notify({"action" : "update_stock" , "item" : product, "quantity" : product.quantity, "update": quantity})
        else:
            return None
        
    def add_observer(self, observer : Observer):
        self.observers.append(observer)
        
    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
            
    def display_items(self):
        self.inventoryviewer.display_items()
        

class InventoryViewer:
    def __init__(self, inventory : Inventory):
        self.inventory = inventory
        
    def display_items(self):
        for item in self.inventory.items:
            print(item.get_details())
            

    
            
        