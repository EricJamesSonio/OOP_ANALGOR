from discount import *
from product import *
from inventory import *


class Cart:
    def __init__(self, discount: Discount, inventory: Inventory):
        self.items: List[Product] = []
        self.discount = discount
        self.inventory = inventory

    def add_to_cart(self, id, quantity):
        product = self.inventory.find_item(id)

        if product is None:
            return "Item doesn't exist"
        if product.quantity < quantity:
            return "Not enough stock in inventory"

        product.quantity -= quantity

        if product.quantity == 0:
            self.inventory.items.remove(product)

        for item in self.items:
            if item.product.id == id:
                item.quantity += quantity
                return f"Updated {item.product.name} quantity in cart."

        self.items.append(Product(product, quantity))
        return f"Added {quantity} of {product.name} to cart."

    def remove_from_cart(self, id, quantity):
        for item in self.items:
            if item.id == id:
                inventory_item = self.inventory.find_item(id)
                if inventory_item:
                    inventory_item.quantity += quantity

                item.quantity -= quantity
                if item.quantity <= 0:
                    self.items.remove(item)
                return
        return None


class CartViewer:
    def __init__(self, cart: Cart):
        self.cart = cart

    def display(self):
        for item in self.cart.items:
            Printer.print_message(
                f"Item : {item.name}, Price : {item.price}, Qtty : {item.quantity}"
            )
