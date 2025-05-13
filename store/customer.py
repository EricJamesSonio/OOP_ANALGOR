from abc import ABC, abstractmethod
from typing import List, Optional


class Customer:
    def __init__(self, name, id, wallet):
        self.wallet = wallet
        self.name = name
        self.id = id
        self.registered = False
