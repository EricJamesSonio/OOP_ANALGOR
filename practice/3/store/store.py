from inventory import *
from observer import *


class Store:
    def __init__(self):
        self.inventory = Inventory()
        self.viewer = InventoryViewer(self.inventory)
        self.observer = RecordViewer()
        self.observer.attach(Logger())
        self.observer.attach(StockAlertSystem())

    def add_product(self, product):
        self.inventory.add_item(product)
        self.observer.notify(f"Added {product.name} to inventory.")

    def sell_product(self, product_id, quantity):
        product = self.inventory.find_item(product_id)
        if product and product.quantity >= quantity:
            self.inventory.update_stock(product_id, quantity)
            if product.quantity < 5:
                self.observer.notify(
                    f"Product {product.name} low stock: {product.quantity}"
                )
        else:
            self.observer.notify(
                f"Product {product_id} not available or insufficient quantity."
            )
