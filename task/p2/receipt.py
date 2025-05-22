from chef import Order


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
        print(f"Change : {process_payment.change}")
