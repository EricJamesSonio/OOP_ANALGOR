from pydantic import BaseModel
from abc import ABC, abstractmethod


class User(BaseModel):
    id: int
    name: str
    age: int


class Product(ABC):
    id: int
    name: str
    price: int


class DigitalProduct(Product):
    def __init__(self):
        super().__init__()


class PhysicalProduct(Product):
    def __init__(self):
        super().__init__()
