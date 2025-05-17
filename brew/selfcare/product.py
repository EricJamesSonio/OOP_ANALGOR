from abc import ABC, abstractmethod
from typing import List

class Product(ABC):
    def __init__(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity
        
    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}"
    
class MainCourse(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)
        
    def get_details(self):
        return super().get_details()
        
class Appetizer(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)
        
    def get_details(self):
        return super().get_details()
    
class Side(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)
        
    def get_details(self):
        return super().get_details()

class Dessert(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)
        
    def get_details(self):
        return super().get_details()
    
class Drinks(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)
        
    def get_details(self):
        return super().get_details()
    
class Add_on(Product, ABC):
    def __init__(self, product : Product, add_on_price):
        super().__init__(product.name, product.code, product.price, product.quantity)
        self.add_on_price = add_on_price
        self.product = product
    
    @abstractmethod
    def get_details(self):
        pass

    def get_price(self):
        return self.product.price + self.add_on_price
    
class Flavor(Add_on, ABC):
    def __init__(self, product, add_on_price, flavor):
        super().__init__(product, add_on_price)
        self.flavor = flavor
        

    def get_details(self):
        return f"{self.product.get_details()} + Flavor : {self.flavor} Add On Price : {self.add_on_price}"
        
class Spicy(Flavor):
    def __init__(self, product, add_on_price, flavor = "Spicy"):
        super().__init__(product, add_on_price, flavor)
        
    def get_details(self):
        return super().get_details()

        
class Sweet(Flavor):
    def __init__(self, product, add_on_price, flavor = "Sweet"):
        super().__init__(product, add_on_price, flavor)
        
    def get_details(self):
        return super().get_details()
    
class Toppings(Add_on, ABC):
    def __init__(self, product, add_on_price, type):
        super().__init__(product, add_on_price)
        self.type = type
        
    def get_details(self):
        return f"{self.product.get_details()} + Type : {self.type} Add On Price : {self.add_on_price}"
    
class Sprinkles(Toppings):
    def __init__(self, product, add_on_price, type = "Sprinkles"):
        super().__init__(product, add_on_price, type)
        
    def get_details(self):
        return super().get_details()
    
class Cream(Toppings):
    def __init__(self, product, add_on_price, type = "Cream"):
        super().__init__(product, add_on_price, type)
        
    def get_details(self):
        return super().get_details()
    
class Helper:
    @staticmethod
    def base_details():
        name = input("Name : ")
        code = input("Code : ")
        price = input("Price : ")
        quantity = input("Quantity : ")
        return name, code, price, quantity
    @staticmethod
    def product_type():
        print("Product type")
        print("[1]. Main Course")
        print("[2]. Sides")
        print("[3]. Drinks")
        print("[4]. Dessert")
        print("[5]. Appetizer")
        choice = input("Enter : ")
        
        if choice == "1":
            return "MainCourse"
        elif choice == "2":
            return "Sides"
        elif choice == "3":
            return "Drinks"
        elif choice == "4":
            return "Dessert"
        elif choice == "5":
            return "Appetizer"
        else:
            return None
        
class ProductFactory:
    def create(self, product_type : Product):
        name, code, price ,quantity = Helper.base_details()
        if product_type == "MainCourse":
            return MainCourse(name, code, price ,quantity)
        elif product_type == "Sides":
            return Side(name, code, price ,quantity)
        elif product_type == "Drinks":
            return Drinks(name, code, price ,quantity)
        elif product_type == "Dessert":
            return Dessert(name, code, price ,quantity)
        elif product_type == "Appetizer":
            return Appetizer(name, code, price ,quantity)
        
    def process(self):
        product_type = Helper.product_type()
        return self.create(product_type)
    

        
        
    
        
