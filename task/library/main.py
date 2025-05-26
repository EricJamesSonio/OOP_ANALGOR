from abc import ABC, abstractmethod
from typing import List


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


class Magazine(LibraryItem):
    def __init__(self, name, id, author):
        super().__init__(name, id, author)


class NewsPaper(LibraryItem):
    def __init__(self, name, id, author):
        super().__init__(name, id, author)


class Library:
    def __init__(self):
        self.items: List["LibraryItem"] = []

    def add_item(self, item: LibraryItem):
        product = self.find_item(item.id)
        if product:
            product.quantity += item.quantity

    def find_item(self, id):
        for item in self.items:
            if item.id == id:
                return item
        return None

    def remove_item(self, id):
        item = self.find_item(id)
        if item:
            self.items.remove(item)
        else:
            return None


class Student:
    pass
