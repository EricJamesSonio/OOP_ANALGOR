from inventory import *


class Store:
    def __init__(self, name, location, owner):
        self.name = name
        self.location = location
        self.owner = owner
        self.inventory = Inventory()
        self.total_sales = []

    def sell_item(self, code, quantity):
        product = self.inventory.find_item(code)
        if product and product.quantity >= quantity:
            total_price = product.price * quantity
            self.inventory.update_stock(product, -quantity)
        elif product and product.quantity == quantity:
            self.inventory.remove_item(product.code)
        else:
            return "Product Does'nt exist"

    def view_total_sales(self):
        print("<-- Total sales __>")
        print(self.total_sales)
