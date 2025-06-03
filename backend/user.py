from abc import ABC, abstractmethod
from discount import DiscountStrategy
from orderprocess import OrderProcessor, Receipt


class User(ABC):
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email

    @abstractmethod
    def get_details(self):
        pass


class Customer(User):
    def __init__(self, name, id, email, discount: DiscountStrategy):
        super().__init__(name, id, email)
        self.discount = discount
        self.wallet = 0
        self.orderhistory = []

    def cash_in(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            return "Insufficient amount"

    def withdraw(self, amount):
        if amount <= self.wallet:
            self.wallet -= amount
            return amount
        return "Insufficient Balance"

    def view_balance(self):
        print(f"Balance : {self.wallet}")

    def get_details(self):
        return f"Customer Name : {self.name}, Id : {self.id}, Email : {self.email}"


class Cashier(User):
    def __init__(self, name, id, email):
        super().__init__(name, id, email)
        self.transactions = []
        self.order_processor = OrderProcessor()

    def process_order(self, pricetopay, customer: Customer, discount: DiscountStrategy):
        result = self.order_processor.process_order(
            pricetopay, customer, discount, self
        )
        if isinstance(result, Receipt):
            return result.create()
        else:
            return result

    def display_transactions(self):
        for transaction in self.transactions:
            print(transaction.create())

    def get_details(self):
        return f"Cashier Name : {self.name}, Id : {self.id}, Email : {self.email}"
