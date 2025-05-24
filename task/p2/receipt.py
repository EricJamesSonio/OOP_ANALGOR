from chef import Order, Cashier, OrderProcessor

"""
class Receipt:
    def get_receipt(self, order: Order, process_total, process_payment):
        print("<-- Receipt -->")
        print(f"Date : {self.order.date}")
        print(f"Time : {self.order.time}")
        print(f"Items : ")
        for order in self.order.orderitem:
            print(order.product.get_details())
        print(f"Total Price : {process_total.total}")
        print(f"Discount Percent : {process_total.discount_percent}")
        print(f"Total Payable : {process_total.total_payable}")
        print(f"Payment : {process_payment.payment}")
        print(f"Change : {process_payment.change}")"""
"""
class Receipt:
    def __init__(self, order: Order, order_processor : OrderProcessor , cashier : Cashier):
        self.order = order
        self.date = self.order.date
        self.order.time = self.order.time
        self.process_total = process_total
        self.process_payment = process_payment
        self.total_price = self.process_total.total
        self.discount_percent = self.process_total.discount_percent
        self.total_payable = self.process_total.total_payable
        self.payment = self.process_payment.payment
        self.change = self.process_payment.change
        self.cashier = cashier
        
    def get_receipt(self):
        print("<-- Receipt -->")
        print(f"Date : {self.date}")
        print(f"Time : {self.time}")
        print(f"Items : ")
        for order in self.order.orderitem:
            print(order.product.get_details())
        print(f"Total Price : {self.total}")
        print(f"Discount Percent : {self.discount_percent}")
        print(f"Total Payable : {self.total_payable}")
        print(f"Payment : {self.payment}")
        print(f"Change : {self.change}")
        print(f"Processed By : {self.cashier.name} : {self.cashier.id}")"""
