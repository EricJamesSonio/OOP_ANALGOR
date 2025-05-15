import copy


class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        product_copy = copy.deepcopy(product)
        product_copy.quantity = quantity
        self.items.append(product_copy)

    def remove_from_cart(self, product_id):
        self.items = [item for item in self.items if item.id != product_id]

    def update_quantity(self, product_id, new_quantity):
        for item in self.items:
            if item.id == product_id:
                item.quantity = new_quantity

    def display_cart(self):
        for item in self.items:
            print(f"{item.name} - Qty: {item.quantity} - Type: {item.get_type()}")
