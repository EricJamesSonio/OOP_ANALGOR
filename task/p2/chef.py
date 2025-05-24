from products import Product, List
from discount import Discount
from inventory import Inventory
import json
import os
import time


class OrderItem:
    def __init__(self, product: Product):
        self.product = product
        self.sales_price = self.product.sales_price
        self.cost_price = self.product.cost_price
        self.quantity = self.product.quantity

    def __str__(self):
        return f"{self.product.name} x{self.quantity} @ {self.sales_price} = {self.quantity * self.sales_price}"


class Order:
    def __init__(self):
        self.orderitem: List[OrderItem] = []
        self.date = time.strftime("%m/%d/%Y")
        self.time = time.strftime("%H/%M/%S")
        self.table_no = 0
        self.numguest = 0
        self.numitems = len(self.orderitem)

    def add_order(self, orderitem: OrderItem):
        self.orderitem.append(orderitem)

    def total_price(self):
        total = 0
        for order in self.orderitem:
            total += order.sales_price * order.quantity

        return total


class Cashier:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.orderprocessor = OrderProcessor()

    def process_order(self, order, discount, payment):
        self.orderprocessor.process_payment(self, order, discount, payment)

    def display_receipts(self):
        self.orderprocessor.order_history.display_receipts()


class DailySales:
    def __init__(self):
        self.sales = []


class OrderProcessor:
    def __init__(self):
        self.order_history = OrderHIstory()

    def process_total(self, order: Order, discount: Discount):
        total = order.total_price()
        discount_percent = discount.percent_discount()
        total_payable = total * discount_percent
        return total, discount_percent, total_payable

    def process_payment(
        self, cashier: Cashier, order: Order, discount: Discount, payment
    ):
        total, discount_percent, total_payable = self.process_total(order, discount)
        if payment >= total_payable:
            change = payment - total_payable
            receipt = Receipt(
                order=order,
                total=total,
                discount_percent=discount_percent,
                total_payable=total_payable,
                payment=payment,
                change=change,
                cashier=cashier,
            )
            self.order_history.receipts.append(receipt)
            return receipt
        else:
            print("❌ Insufficient payment.")
            return None

    def display_receipts(self):
        self.order_history.display_receipts()


class OrderHIstory:
    def __init__(self):
        self.receipts: List["Receipt"] = []

    def display_receipts(self):
        for receipt in self.receipts:
            receipt.get_receipt()


class ReceiptGenerator:
    pass


class Receipt:
    def __init__(
        self, order, total, discount_percent, total_payable, payment, change, cashier
    ):
        self.receipt_no = f"R-{get_next_receipt_no():04d}"
        self.order = order
        self.date = order.date
        self.time = order.time
        self.total = total
        self.discount_percent = discount_percent
        self.total_payable = total_payable
        self.payment = payment
        self.change = change
        self.cashier = cashier

    def get_receipt(self):
        print(f"<-- Receipt #{self.receipt_no} -->")
        print(f"Date : {self.date}")
        print(f"Time : {self.time}")
        print("Items:")
        for item in self.order.orderitem:
            print(item.product.get_details())
        print(f"Total Price : {self.total}")
        print(f"Discount Percent : {self.discount_percent}")
        print(f"Total Payable : {self.total_payable}")
        print(f"Payment : {self.payment}")
        print(f"Change : {self.change}")
        print(f"Processed By : {self.cashier.name} : {self.cashier.id}")


def get_next_receipt_no():
    file_path = "receipt_counter.json"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump({"last_receipt_no": 0}, f)

    with open(file_path, "r") as f:
        data = json.load(f)

    data["last_receipt_no"] += 1

    with open(file_path, "w") as f:
        json.dump(data, f)

    return data["last_receipt_no"]


class Sales:
    def __init__(self, receipt: Receipt):
        self.receipt = receipt

    def get_profit(self):
        profit = 0
        for receipt in self.receipt:
            profit += (
                receipt.order.orderitem.sales_price - receipt.order.orderitem.cost_price
            )
        return profit

    def get_total(self):
        return self.receipt.total_payable


class DailySales:
    def __init__(self):
        self.sales: List[Sales] = []

    def find_sales(self, receipt_no):
        for sale in self.sales:
            if sale.receipt.receipt_no == receipt_no:
                return sale
        return None

    def add_sales(self, sales: Sales):
        exist = self.find_sales(sales.receipt.receipt_no)
        if exist:
            return "Already Exist"
        else:
            self.sales.append(sales)

    def total_prices(self):
        total = 0
        for sale in self.sales:
            total += sale.get_total()

    def total_profit(self):
        profit = 0
        for sale in self.sales:
            profit += sale.get_profit()
