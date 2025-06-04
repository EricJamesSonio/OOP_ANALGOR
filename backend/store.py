from inventory import Inventory


class Store:
    def __init__(self, name, id, location, description):
        self.name = name
        self.id = id
        self.location = location
        self.description = description
        self.inventory = Inventory()

    def edit_description(self, new_description):
        self.description = new_description

    def get_details(self):
        return f"Store Name : {self.name}, Id : {self.id}, Location : {self.location}, Description : {self.description}"

    def add_item(self, item):
        self.inventory.add_item(item)

    def find_item(self, id):
        self.inventory.find_item(id)

    def remove_item(self, id):
        self.inventory.remove_item(id)

    def reduce_stock(self, id, quantity):
        self.inventory.reduce_stock(id, quantity)

    def increase_stock(self, id, quantity):
        self.inventory.increase_stock(id, quantity)

    def display_items(self):
        self.inventory.display_items()
