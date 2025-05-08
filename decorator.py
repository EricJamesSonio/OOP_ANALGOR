from abc import ABC, abstractmethod
from typing import List, Optional


class Guitar(ABC):
    def __init__(self, name, wood, type):
        self.name = name
        self.wood = wood
        self.type = type

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def price(self):
        pass


class Fender(Guitar):
    def __init__(self, name, wood, type, brand="Fender"):
        super().__init__(name, wood, type, brand)
        self.brand = brand

    def get_details(self):
        return f"Name : {self.name}, Wood : {self.wood}, Type : {self.type}, Brand : {self.brand}"

    def price(self):
        return 1000


class LesPaul(Guitar):
    def __init__(self, name, wood, type, brand="Les Paul"):
        super().__init__(name, wood, type, brand)
        self.brand = brand

    def get_details(self):
        return f"Name : {self.name}, Wood : {self.wood}, Type : {self.type}, Brand : {self.brand}"

    def price(self):
        return 2000


class GuitarDecorator(Guitar):
    def __init__(self, name, wood, type, guitar: Guitar):
        self._guitar = guitar

    def get_details(self):
        pass

    def price(self):
        pass


class VintageTuner(GuitarDecorator):
    def __init__(self, name, wood, type, guitar):
        super().__init__(name, wood, type, guitar)

    def get_details(self):
        return self._guitar.get_details() + ",Vintage Tuner"

    def price(self):
        return self._guitar.price() + 1000


class ClassicTuner(GuitarDecorator):
    def __init__(self, name, wood, type, guitar):
        super().__init__(name, wood, type, guitar)

    def get_details(self):
        return self._guitar.get_details() + ",Classic Tuner"

    def price(self):
        return self._guitar.price() + 300


class SilverTuner(GuitarDecorator):
    def __init__(self, name, wood, type, guitar):
        super().__init__(name, wood, type, guitar)

    def get_details(self):
        return self._guitar.get_details() + ",Silver Tuner"

    def price(self):
        return self._guitar.price() + 200
