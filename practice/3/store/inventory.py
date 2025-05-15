class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product_id):
        self.items = [p for p in self.items if p.id != product_id]

    def find_item(self, product_id):
        return next((p for p in self.items if p.id == product_id), None)

    def update_stock(self, product_id, amount):
        product = self.find_item(product_id)
        if product:
            product.quantity -= amount


class InventoryViewer:
    def __init__(self, inventory):
        self.inventory = inventory

    def display_inventory(self):
        for item in self.inventory.items:
            print(f"{item.name} - {item.quantity} available - {item.get_type()}")
