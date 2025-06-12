from datetime import datetime
from typing import List
from abc import abstractmethod, ABC


class UnliWingsApp:
    def __init__(self):
        self.order_items: List[Order] = []
        self.total_sales = 0
        self.menu_items = {
            ChickenWings: [
                FriedChickenWings("Fried Chicken Wings", 1, Small(), 150, 10),
                BBQChickenWings("BBQ Chicken Wings", 1, Small(), 180, 10),
                BakedBuffaloWings("Baked Buffalo Wings", 1, Small(), 200, 10),
            ],
        }


class Menuitem:
    def __init__(self, name, id, size: "SizeStrategy", price, quantity):
        self.name = name
        self.id = id
        self.size = size
        self.price = price
        self.quantity = quantity

    def get_details(self):
        return f"Name : {self.name}, Id : {self.id}, Size : {self.size} Price : {self.price}, Quantity : {self.quantity}"


class ChickenWings(Menuitem):
    pass


class FriedChickenWings(ChickenWings):
    pass


class BakedBuffaloWings(ChickenWings):
    pass


class BBQChickenWings(ChickenWings):
    pass


class Pizza(Menuitem):
    pass


class SizeStrategy:
    def __init__(self):
        self.add = None


class Small(SizeStrategy):
    def __init__(self):
        super().__init__()
        self.add = 1.2


class Medium(SizeStrategy):
    def __init__(self):
        super().__init__()
        self.add = 1.5


class Large(SizeStrategy):
    def __init__(self):
        super().__init__()
        self.add = 1.7


class OrderItem:
    def __init__(self, product: Menuitem):
        self.product = product
        self.product_totalprice = product.price * product.size.add * product.quantity

    def get_details(self):
        return f"Name : {self.product.name}, Id : {self.product.id}, Total Price : {self.product_totalprice}"


class Order:
    def __init__(self):
        self.orders: List[OrderItem] = []
        self.timestamp = datetime.now()
        self.time = self.timestamp.time()
        self.date = self.timestamp.date()

    def calculate_total(self):
        total = 0
        for order in self.orders:
            total += order.product_totalprice

        return total

    def get_details(self):
        pass


class DiscountStrategy:
    def __init__(self):
        self.discount_percent = 0


class SeniorDiscount(DiscountStrategy):
    def __init__(self):
        super().__init__()
        self.discount_percent = 0.90


class PWDDiscount(DiscountStrategy):
    def __init__(self):
        super().__init__()
        self.discount_percent = 0.85


class PaymentStrategy(ABC):
    @abstractmethod
    def pay_amount(self, amount):
        pass


class Cash(PaymentStrategy):
    def pay_amount(self, amount):
        return amount


class Gcash(PaymentStrategy):
    def pay_amount(self, amount):
        return amount * 0.90


class OrderProcessor:
    def __init__(self):
        self.completed_orders = []

    def process_order(
        self, order: Order, amount, payment: PaymentStrategy, discount: DiscountStrategy
    ):
        discount_percent = discount.discount_percent
        total_price = order.calculate_total()
        discounted_price = discount_percent * total_price
        pay_amount = payment.pay_amount(amount)
        if pay_amount >= discounted_price:
            change = pay_amount - discounted_price
        else:
            return "Not enough amount "


class Receipt:
    _receipt_counter = 0

    def __init__(
        self,
        order: Order,
        discount_percent,
        total_price,
        discounted_price,
        pay_amount,
        change,
    ):
        self.order = order
        self.discount_percent = discount_percent
        self.change = change
        self.total_price = total_price
        self.discounted_price = discounted_price
        self.pay_amount = pay_amount
        self.receipt_no = Receipt._receipt_counter
        Receipt._receipt_counter += 1

    def create(self):
        print("< -- Receipt -- >")
        print(f"Date : {self.order.date}")
        print(f"Time : {self.order.time}")
        print(f"Receipt No :  {self.receipt_no}")
        print("Order Items : ")
        for item in self.order:
            item.get_details()
        print(f"Total Price : {self.total_price} ")
        print(f"Total Discount Percent : {self.discount_percent}")
        print(f"Total Payable : {self.discounted_price}")
        print(f"Change : {self.change}")
        print("Thankyou For Buying!")
