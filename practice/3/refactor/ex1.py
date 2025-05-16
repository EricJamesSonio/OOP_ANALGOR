from abc import ABC, abstractmethod
from typing import List

# ------------- Book -------------- #


class Book(ABC):
    def __init__(self, title, code, price, quantity):
        self.title = title
        self.code = code
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_details(self):
        pass


class ScienceBook(Book):
    def get_details(self):
        return f"Title : {self.title}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}"


class MathBook(Book):
    def get_details(self):
        return f"Title : {self.title}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}"


class EnglishBook(Book):
    def get_details(self):
        return f"Title : {self.title}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}"


# ------------- Member -------------- #
class Member:
    def __init__(self, name, id, email, payment: "Payment"):
        self.name = name
        self.id = id
        self.books: List[Book] = []
        self.cart = None
        self.email = email
        self.wallet = Wallet(self)
        self.payment = payment
        self.discount = None
        self.observer = Email()
    
    def rent_book(self, item, quantity):
        self.cart.add_to_cart(item, quantity)

    def request_return(self, item, cashier: "Cashier"):
        request = {"name": self.name, "id": self.id, "item": item}
        cashier.get_request(request)

    def return_book(self, code, cashier: "Cashier"):
        for book in self.books:
            if book.code == code:
                self.request_return(book, cashier)
                self.observer.update(
                    {"action": "returned_item", "item": book, "customer": self.id}
                )
                self.books.remove(book)
            else:
                return
        return None

    def cash_in(self, amount):
        self.wallet.cash_in(amount)

    def display_balance(self):
        self.wallet.display_balance()

    def pay(self, amount):
        self.payment.pay(amount)
        
    def start_shopping(self):
        self.cart = self.store.borrow_cart(self.id)
        if self.cart:
            print(f"Cart #{self.cart.cart_id} assigned to member {self.id}")

    def finish_shopping(self):
        if self.cart:
            self.store.return_cart(self.id)
            self.cart = None


class Cart:
    def __init__(self, store: "BookStore", cart_id):
        self.store = store
        self.items: list[Book] = []
        self.cart_id = cart_id

    def add_to_cart(self, item, quantity):
        product = self.store.inventory.find_item(item.code)
        if product and product.quantity >= quantity:
            clone = type(product)(product.title, product.code, product.price, quantity)
            self.items.append(clone)
            self.store.inventory.update_stock(product.code, -quantity)
        else:
            return None

    def remove_from_cart(self, code):
        product = self.store.inventory.find_item(code)
        if product:
            self.items.remove(product)
            self.store.inventory.update_stock(product.code, product.quantity)
        else:
            return None

    def change_quantity(self, code, quantity):
        product = self.store.inventory.find_item(code)
        if product and product.quantity > quantity:
            diff = product.quantity - quantity
            product.quantity -= diff
            self.store.inventory.update_stock(product.code, diff)
        elif product and product.quantity < quantity:
            diff = product.quantity - quantity
            product.quantity += diff
            self.store.inventory.update_stock(product.code, -diff)
        else:
            return None
    
    def clear_cart(self):
        self.items.clear()

    def display_cart(self):
        for item in self.items:
            print(item.get_details())


class Teacher(Member):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.discount = VIPDiscount()

    def rent_book(self, item, quantity):
        return super().rent_book(item, quantity)


class Student(Member):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.discount = RegularDiscount()

    def rent_book(self, item, quantity):
        return super().rent_book(item, quantity)


# ------------- Wallet & Payment-------------- #


class Payment(ABC):
    @abstractmethod
    def pay(self, price):
        pass


class Cash(Payment):
    def pay(self, price):
        return price


class CreditCard(Payment):
    def pay(self, price):
        return price * 0.98


class Wallet:
    def __init__(self, user: Member):
        self.balance = 0
        self.user = user
        self.observers: List["Observer"] = []
        self.payment = self.user.payment

    def cash_in(self, amount):
        if amount > 0:
            self.balance += amount
            self.notify({"action": "cash_in", "amount": amount})
        else:
            return None

    def add_observer(self, observer: "Observer"):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def display_balance(self):
        print(self.balance)

    def pay(self, amount):
        self.user.pay(amount)


# ------------- Discount -------------- #


class Discount(ABC):
    def apply_discount(self, price):
        pass


class RegularDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.90


class VIPDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.85


# ------------- BookStore -------------- #


class Storage:
    def __init__(self):
        self.items: List[Book] = []
        self.observers: List[Observer] = []

    def find_item(self, code):
        for item in self.items:
            if item.code == code:
                return item
        return None

    def add_book(self, item):
        product = self.find_item(item.code)
        if product:
            total = product.quantity + item.quantity
            product.quantity += item.quantity
            self.notify(
                {
                    "action": "add_stock",
                    "item": product,
                    "added": item.quantity,
                    "quantity": total,
                }
            )
        else:
            self.items.append(item)
            self.notify(
                {"action": "add_item", "item": product, "quantity": item.quantity}
            )

    def remove_item(self, code):
        product = self.find_item(code)
        if product:
            self.items.remove(product)
            self.notify(
                {
                    "action": "removed_item",
                    "item": product,
                    "quantity": product.quantity,
                }
            )
        else:
            return None

    def update_stock(self, code, quantity):
        product = self.find_item(code)
        if product:
            previous = product.quantity
            total = product.quantity + quantity
            product.quantity += quantity
            self.notify(
                {
                    "action": "updated_item",
                    "item": product,
                    "quantity": total,
                    "prev": previous,
                }
            )
        else:
            return None

    def add_observer(self, observer: "Observer"):
        self.observers.append(observer)


class StorageViewer:
    def __init__(self, storage: Storage):
        self.storage = storage

    def display_storage(self):
        for item in self.storage.items:
            print(item.get_details())

# ------------- Store -------------- #


class BookStore:
    def __init__(self):
        self.inventory = Storage()
        self.inventoryviewer = StorageViewer(self.inventory)
        self.available_carts = [Cart(self, cart_id) for cart_id in range(100)]
        self.in_use_cart = {}

    def add_item(self, item):
        self.inventory.add_book(item)

    def remove_item(self, code):
        self.inventory.remove_item(code)

    def find_item(self, code):
        return self.inventory.find_item(code)

    def display_storage(self):
        self.inventoryviewer.display_storage()

    def rent_book(self, code):
        book = self.inventory.find_item(code)
        if book:
            return book
        else:
            return None
        
    def borrow_cart(self, member_id):
        if member_id in self.in_use_cart:
            return self.in_use_cart[member_id]

        if self.available_carts:
            cart = self.available_carts.pop()
            self.in_use_cart[member_id] = cart
            return cart
        else:
            return None


    def return_cart(self, member_id):
        if member_id in self.in_use_cart:
            cart = self.in_use_cart.pop(member_id)
            self.available_carts.append(cart)
            
class StoreService:
    def __init__(self, store : BookStore):
        self.store = store
        
    def assign_cart(self, member):
        self.store.borrow_cart(member.id)
        
        

# ------------- Cashier -------------- #


class Cashier:
    request_no = 0

    def __init__(self, store: "BookStore"):
        self.store = store
        self.requests = []
        self.orderprocessor = OrderProcessor()
        self.request_no = Cashier.request_no
        self.requestviewer = RequestViewer(self)
        self.customerrecords = CustomerRecords()

    def sell_book(self, code, days, customer: "Member"):
        product = self.store.find_item(code)
        if product and days >= 7:
            discount_price = customer.discount.apply_discount(product.price)
            if customer.wallet.balance >= discount_price:
                receipt = self.orderprocessor.process_order(product, customer.wallet)
                self.customerrecords.add_customer(customer)
                return receipt
            else:
                return None

    def get_request(self, message):
        request_no = self.request_no + 1
        self.request_no += 1
        self.requests.append(
            {
                "number": request_no,
                "name": message["name"],
                "id": message["id"],
                "item" : message["item"],
                "message": message,
            }
        )

    def find_and_approve_request(self, request_no: int):
        for req in self.requests:
            if req["number"] == request_no:
                customer = self.customerrecords.find_customer(req["id"])
                if customer:
                    self.approve_return(req["item"], customer)
                    self.requests.remove(req)
                    customer.observer.update({"action" : "approved_return", "item" : req["item"]})
                    print(f"Request {request_no} approved.")
                else:
                    print("Customer not found.")
                return
        print("Request not found.")

    def choose_request(self):
        print("< -- Return Requests -- >")
        self.display_requests()
        try:
            choice = int(input("Enter Request No to approve: "))
            self.find_and_approve_request(choice)
        except ValueError:
            print("Invalid input.")

    def approve_return(self, item, customer: Member):
        self.store.add_item(item)
        self.customer.observer.update({"action": "approved_return", "item": item})

    def display_requests(self):
        self.requestviewer.display_requests()

    def display_customers(self):
        self.customerrecords.display_customers()


class RequestViewer:
    def __init__(self, cashier: Cashier):
        self.cashier = cashier

    def display_requests(self):
        for req in self.cashier.requests:
            print(req)


class CustomerRecords:
    customer_counter = 0

    def __init__(self):
        self.customers: List["Member"] = []
        self.observer = LoggerCustomer()
        self.observerviewer = Observerviewer(self.observer)

    def find_customer(self, id):
        for customer in self.customers:
            if customer.id == id:
                return customer
        return None

    def add_customer(self, customer: "Member"):
        CustomerRecords.customer_counter += 1
        customer.customer_no = CustomerRecords.customer_counter
        self.customers.append(customer)
        self.observer.update(
            {
                "action": "add_customer",
                "customer_no": customer.customer_no,
                "name": customer.name,
            }
        )

    def display_customers(self):
        self.observerviewer.display_records()


# ------------- Orderprocessor -------------- #


class OrderProcessor:
    def __init__(self):
        self.orderhistory = OrderHistory()

    def process_order(self, product, wallet: Wallet):
        if wallet.balance >= product.price:
            total_price = product.price
            change = wallet.balance - total_price
            wallet.balance -= total_price
            receipt = Receipt(wallet.balance, product, total_price, change)
            self.orderhistory.orderrecords.append(receipt)
            return receipt
        else:
            return "Insufficient Balance"


class OrderHistory:
    def __init__(self):
        self.orderrecords: List[Receipt] = []

    def display_orders(self):
        for record in self.orderrecords:
            print(record)

        


# ------------- Receipt -------------- #


class Receipt:
    receipt_no = 0

    def __init__(self, payment_amount, product, total_price, change):
        self.payment_amount = payment_amount
        self.product = product
        self.total_price = total_price
        self.change = change
        Receipt.receipt_no += 1
        self.receipt_no = Receipt.receipt_no

    def __str__(self):
        return (
            f"<--- Receipt --->\n"
            f"Receipt No   : {self.receipt_no}\n"
            f"Item         : {self.product.title}\n"
            f"Price        : ₱{self.total_price:.2f}\n"
            f"Paid Amount  : ₱{self.payment_amount:.2f}\n"
            f"Change       : ₱{self.change:.2f}\n"
            f"Thanks for shopping!\n"
        )


# ------------- Observer -------------- #


class Observer(ABC):
    def __init__(self):
        self.records = []

    @abstractmethod
    def update(self, message):
        pass


class LoggerStorage(Observer):
    def update(self, message):
        if message["action"] == "add_item":
            item = message["item"]
            quantity = message["quantity"]
            record = f"Added Item : {item.name}, Quantity : {quantity}"
            self.records.append(record)
        elif message["action"] == "removed_item":
            item = message["item"]
            quantity = message["quantity"]
            record = f"Removed Item : {item.name}, Quantity : {quantity}"
            self.records.append(record)
        else:
            return None


class LoggerCustomer(Observer):
    def update(self, message):
        if message["action"] == "add_customer":
            customer_no = message["customer_no"]
            name = message["name"]
            record = f"Added Customer : {name} Customer NO : {customer_no}"
            self.records.append(record)
        else:
            return None


class StockAlertSystem(Observer):
    def update(self, message):
        if message["action"] == "add_stock":
            item = message["item"]
            quantity = message["added"]
            total = message["quantity"]
            record = f"Added Stock : {item.name}, Added Quantity : {quantity}, Total : {total}"
            self.records.append(record)
        elif message["action"] == "updated_item":
            item = message["item"]
            quantity = message["quantity"]
            prev = message["prev"]
            record = f"Updated Item : {item.name}, Quantity : {quantity}, Previous Qtty : {prev}"
            self.records.append(record)
        else:
            return None


class Email(Observer):
    @abstractmethod
    def update(self, message):
        if message["action"] == "returned_item":
            item = message["item"]
            record = f"Returning item : {item.title}"
            self.records.append(record)
        elif message["action"] == "approved_return":
            item = message["item"]
            record = f"Approved Return! Item : {item.name}"
            self.records.append(record)
        else:
            return None


class SMS(Email):
    def update(self, message):
        return super().update(message)()


class InApp(Email):
    def update(self, message):
        return super().update(message)


class Observerviewer:
    def __init__(self, observer: Observer):
        self.observer = observer

    def display_records(self):
        for record in self.observer.records:
            print(record)



