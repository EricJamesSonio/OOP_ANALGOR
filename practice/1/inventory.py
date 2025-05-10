from product import *


class Inventory:
    def __init__(self):
        self.products: List[Product] = []

    def add_item(self, item: Product):
        product = self.find_item(item.code)
        if product:
            product.quantity += item.quantity
        else:
            self.products.append(item)

    def remove_item(self, code):
        product = self.find_item(code)
        if product:
            self.products.remove(product)
        else:
            return "Product Doesnt exist"

    def update_stock(self, code, quantity):
        product = self.find_item(code)
        if product and product.quantity > quantity:
            product.quantity -= quantity
        elif product and product.quantity == quantity:
            self.remove_item(product.code)
        else:
            return "Doesn't exist"

    def find_item(self, code):
        for existing_item in self.products:
            if existing_item.code == code:
                return existing_item
