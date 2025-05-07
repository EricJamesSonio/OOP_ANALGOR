from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class User(Observer):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def update(self):
        pass


class InventoryManager(User):
    def __init__(self, name, id):
        super().__init__(name, id)

    def update(self):
        return f"Inventory Manager : {self.name} is notified! "


class StoreManager(User):
    def __init__(self, name, id):
        super().__init__(name, id)

    def update(self):
        return f"Store Manager : {self.name} is notified! "


class Customer(User):
    def __init__(self, name, id):
        super().__init__(name, id)

    def update(self):
        return f"Customer : {self.name} is notified! "
