from baseproduct import *
from observer import *
from typing import List
from product import *
import json

class Inventory:
    def __init__(self, filepath = None):
        self.items: List[ProductBase] = []
        self.observers: List[Observer] = []
        self.threshold = 10
        self.filepath = filepath
        if filepath:
            self.load_items_from_file()

    def find_item(self, code):
        for item in self.items:
            if item.code == code:
                return item
        return None

    def add_item(self, item):
        product = self.find_item(item.code)
        if product:
            product.quantity += item.quantity
            self.notify(
                {
                    "action": "add_stock",
                    "item": product,
                    "quantity": item.quantity,
                    "total": product.quantity,
                }
            )
        else:
            self.items.append(item)
            self.notify({"action": "add_item", "item": item, "quantity": item.quantity})
            
        self.stock_warning()
        self.save_items_to_file()

    def remove_item(self, code):
        product = self.find_item(code)
        if product:
            self.items.remove(product)
            self.notify(
                {
                    "action": "removed_item",
                    "item": product,
                    "quantity": product.quantity,
                }
            )
            self.save_items_to_file()
        else:
            return None
        
        self.stock_warning()

    def update_stock(self, code, quantity):
        product = self.find_item(code)
        if not product:
            return None

        product.quantity += quantity  # This handles both + and - changes

        self.notify({
            "action": "add_stock" if quantity > 0 else "minus_stock",
            "item": product,
            "update": quantity,
            "quantity": product.quantity,
        })

        self.stock_warning()
        self.save_items_to_file()

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
            
    def set_threshold(self, threshold):
        self.threshold = threshold
        
    def is_low_stock(self, quantity):
        return quantity <= self.threshold
    
    def stock_warning(self):
        for item in self.items:
            if self.is_low_stock(item.quantity):
                self.notify({
                    "action": "low_stock_warning",
                    "item": item,
                    "quantity": item.quantity
                })
                
    def load_items_from_file(self):
        if not self.filepath:
            return
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
                self.items = [ProductBase.from_dict(item) for item in data]
        except FileNotFoundError:
            self.items = []
        except Exception as e:
            print(f"Failed to load inventory file: {e}")


    def save_items_to_file(self):
        if not self.filepath:
            return
        try:
            with open(self.filepath, "w") as f:
                json.dump([item.to_dict() for item in self.items], f, indent=4)
        except Exception as e:
            print(f"Failed to save inventory file: {e}")

class IngredientInventory(Inventory):
    def __init__(self):
        super().__init__(filepath = "ingredientinventory.json")

class BeverageInventory(Inventory):
    def __init__(self):
        super().__init__(filepath = "beverageinventory.json")

class FoodMenuInventory(Inventory):
    def __init__(self):
        super().__init__(filepath = "foodmenuinventory.json")

class InventoryViewer:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def display_inventory(self):
        for item in self.inventory.items:
            print(item.get_details())

