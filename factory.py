from abc import ABC, abstractmethod


class Drink(ABC):
    def __init__(self, name, code, flavor, volume):
        self.name = name
        self.code = code
        self.volume = volume
        self.flavor = flavor

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def serve(self):
        pass


class Coke(Drink):
    def __init__(self, name, code, flavor, volume):
        super().__init__(name, code, flavor, volume)

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Flavor : {self.flavor}, Volume : {self.volume}"

    def serve(self):
        return "Coke is serving..."


class Lemonade(Drink):
    def __init__(self, name, code, flavor, volume):
        super().__init__(name, code, flavor, volume)

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Flavor : {self.flavor}, Volume : {self.volume}"

    def serve(self):
        return "Lemonade is serving..."


class DrinkFactory:

    def helper(self):
        print("<-- Drink Details -->")
        name = input("Name : ")
        code = input("Code : ")
        flavor = input("Flavor : ")
        volume = input("Volume : ")
        return name, code, flavor, volume

    def create(self):
        print("<-- Drink Type -->")
        print("[1]. Coke")
        print("[2]. Lemonade")
        choice = input("Enter choice : ")

        name, code, flavor, volume = self.helper()

        if choice == "1":
            return Coke(name, code, flavor, volume)
        elif choice == "2":
            return Lemonade(name, code, flavor, volume)
        else:
            return "None"


factory = DrinkFactory()
print(factory.create())
