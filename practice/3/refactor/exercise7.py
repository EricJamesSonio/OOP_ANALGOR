from abc import ABC, abstractmethod
from typing import List, Optional

# Desk 

class Desk(ABC):
    def __init__(self, code,price):
        self.price = price
        self.code = code
        
        
class Hotdesk(Desk):
    def __init__(self, code,price = 100):
        super().__init__(price, code)
        
        
class DedicatedDesk(Desk):
    def __init__(self,code, price = 200):
        super().__init__(price, code)
        
class PrivateOffice(Desk):
    def __init__(self, code,price = 500):
        super().__init__(price, code)

#Discount strategy

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass
    
class RegularDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price
    
class StartUpDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.90
    
class EnterpriseUserDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.80

# Payment

class Payment:    
    def __init__(self, customer):
        self.customer = customer
        
    def pay(self, amount, price_to_pay):
        pre_total = self.customer.discount.apply_discount(price_to_pay)
        total = pre_total - amount
        return total

# User

class User:
    def __init__(self, name, email, sms,discount : DiscountStrategy, payment : Payment,desk : Desk, store : 'BookingWorkspace'):
        self.discount = discount
        self.desk = desk
        self.name = name
        self.payment = payment
        self.store = store
        self.cart = Renting(self, self.store)
        self.wallet = Wallet(self)
        self.desk = []
        self.cash = 0
        self.email = email
        self.sms = sms
        
    def pay(self, amount, price_to_pay):
        return self.payment.pay(amount, price_to_pay)
    
    def cash_in(self, amount):
        self.wallet.cash_in(amount)
        
    def rent_desk(self, item, amount, hours):
        self.cart.bought_desk(self, item, amount, hours)
        
# wallet

class Wallet:
    def __init__(self, user : User):
        self.user = user
        
    def cash_in(self, amount):
        if amount > 0:
            self.user.cash += amount
        else:
            return None
    
        
        
class Renting:
    def __init__(self, user : User, bookingworkspace : 'BookingWorkspace'):
        self.bookingworkspace = bookingworkspace
        self.user = user
        self.records = []
        self.observers : List[Observer] = []
        
    def bought_desk(self, item, amount, hours):
        price = self.bookingworkspace.give_desk(item, hours)
        paid = self.user.pay(amount, price)
        if paid >= 0:
            self.user.desk.append(item)
            self.notify({"action" : "bought" , "item" : item, "price" : price})
        else:
            return None     
        
    def display_desk(self):
        for desk in self.user.desk:
            print(desk)
            
    def add_observer(self, observer):
        self.observers.append(observer)
        
    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
        

# inventory

class Inventory:
    def __init__(self):
        self.items : List[Desk] = []
        self.observers: List[Observer] = []
        self.recordviewer = RecordViewer
        
    def find_item(self, code):
        for item in self.items:
            if item.code == code:
                return item
        return None

    def add_item(self, desk):
        product = self.find_item(desk.code)
        if product:
            return 
        else:
            self.items.append(desk)
            self.notify({"action" : "add_item", "item" : desk})
            
    def remove_item(self, code):
        product = self.find_item(code)
        if product:
            self.items.remove(product)
            self.notify({"action" : "removed_item", "item" : product})
        else:
            return None
        
    def add_observer(self, observer : 'Observer'):
        self.observer.append(observer)
        
    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
            
    
            
class InventoryViewer:
    def __init__(self, inventory : Inventory):
        self.inventory = inventory
        
    def display_inventory(self):
        for item in self.inventory.items:
            print(item)

# workspace booking

class BookingWorkspace:
    def __init__(self):
        self.inventory = Inventory()
        self.inventoryviewer = InventoryViewer(self.inventory)
        self.logger = Logger()
        self.inventory.add_observer(self.logger)
        self.recordviewer = RecordViewer(self.logger)
        
    def add_item(self, desk):
        self.inventory.add_item(desk)
        
    def find_item(self, code):
        return self.inventory.find_item(code)
    
    def remove_item(self, code):
        self.inventory.remove_item(code)
        
    def give_desk(self, item : Desk, hours : int):
        desk = self.inventory.find_item(item.code)
        if desk:
            total = desk.price * hours
            return total
        else:
            return None

    def display_inventory(self):
        self.inventoryviewer.display_inventory()
        
    def display_records(self):
        self.recordviewer.display_records()
        
    
            
# observer

class Observer(ABC):
    def __init__(self):
        self.records = []
    @abstractmethod
    def update(self, message):
        pass
    
class Logger(Observer):
    def update(self, message):
        if message["action"] == "add_item":
            item = message["item"]
            record = f"Added Item : {item.name} in the inventory"
            self.records.append(record)
        elif message["action"] =="removed_item":
            item = message["item"]
            record = f"Removed Item : {item.name} in the inventory"
            self.records.append(record)
        else:
            return None
        
class Email(Observer):
    def __init__(self, email):
        self.email = email
        
    def update(self, message):
        if message["action"] == "bought":
            item = message["item"]
            price = message["price"]
            record = f"Bought Desk : {item.name} Price : {price}"
            self.records.append(record)
        else:
            return None
    
class SMS(Observer):
    def __init__(self, sms):
        self.sms = sms
        
    def update(self, message):
        if message["action"] == "bought":
            item = message["item"]
            price = message["price"]
            record = f"Bought Desk : {item.name} Price : {price}"
            self.records.append(record)
        else:
            return None
        
class InApp(Observer):
    def __init__(self, contact):
        self.contact = contact
        
    def update(self, message):
        if message["action"] == "bought":
            item = message["item"]
            price = message["price"]
            record = f"Bought Desk : {item.name} Price : {price}"
            self.records.append(record)
        else:
            return None
        
class RecordViewer:
    def __init__(self, observer: Observer):
        self.observer = observer
        
    def display_records(self):
        for record in self.observer.records:
            print(record)



        


    