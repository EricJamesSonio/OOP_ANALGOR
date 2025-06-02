from abc import ABC, abstractmethod
from typing import List


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name : {self.name}, Id : {self.id}"


class Customer(User):
    def __init__(self, name, id):
        super().__init__(name, id)


class LibraryItem(ABC):
    def __init__(self, name, id, author):
        self.name = name
        self.id = id
        self.author = author

    @abstractmethod
    def get_details(self):
        pass


class Book(LibraryItem):
    def __init__(self, name, id, author):
        super().__init__(name, id, author)

    def get_details(self):
        return f"Name : {self.name}, Id : {self.id}, Author : {self.author}"


class Magazine(LibraryItem):
    def __init__(self, name, id, author):
        super().__init__(name, id, author)

    def get_details(self):
        return super().get_details()


class LibraryStore:
    def __init__(self, name, id, location):
        self.name = name
        self.id = id
        self.location = location
        self.inventory = Inventory()

    def add_item(self, item):
        self.inventory.add_item(item)

    def remove_item(self, id):
        self.inventory.remove_item(id)

    def find_item(self, id):
        self.inventory.find_item(id)

    def display_items(self):
        self.inventory.display()


class Inventory:
    def __init__(self, librarystore=LibraryItem):
        self.items: List[LibraryItem]
        self.librarystore = librarystore

    def find_item(self, id):
        for item in self.items:
            if item.id == id:
                return item
        return None

    def add_item(self, item: LibraryItem):
        self.items.append(item)

    def remove_item(self, id):
        product = self.find_item(id)
        if product:
            self.items.remove(product)
        else:
            return None

    def display_items(self):
        for item in self.items:
            print(item.get_details())
