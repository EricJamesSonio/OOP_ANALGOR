from abc import ABC, abstractmethod
from typing import List, Optional
from inventory import *


class Store:
    _instance = None
    _initialized = False

    def __new__(cls, name=None, location=None, owner=None):
        if cls._instance is None:
            cls._instance = super(Store, cls).__new__(cls)
            print("Creating the singleton instance")
        return cls._instance

    def __init__(self, name=None, location=None, owner=None):
        if not self._initialized:
            self.name = name
            self.location = location
            self.owner = owner
            self.inventory = Inventory()
            Store._initialized = True

    def add_new_item(self, item):
        self.inventory.add_item(item)
