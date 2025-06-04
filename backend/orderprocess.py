from store import Store
from discount import DiscountStrategy
from user import Cashier, Customer


class OrderProcessor:
    def process_order(
        self,
        pricetopay,
        customer: Customer,
        discount: DiscountStrategy,
        cashier: Cashier,
    ):
        discounted_price = discount.apply_discount(pricetopay)
        amount = customer.wallet
        if discounted_price <= customer.wallet:
            change = discounted_price - customer.wallet
            customer.wallet -= discounted_price
            receipt = Receipt(
                pricetopay,
                amount,
                change,
                discount.discount_percent,
                discounted_price,
                cashier,
            )
            cashier.transactions.append(receipt)
            return receipt
        else:
            return "Insufficient Balance"


class Receipt:
    _receipt_counter = 0

    def __init__(
        self,
        price_to_pay,
        paid_amount,
        change,
        discount_percent,
        discounted_price,
        cashier,
    ):
        self.pricetopay = price_to_pay
        self.paid_amount = paid_amount
        self.change = change
        self.discount_percent = discount_percent
        self.discount_price = discounted_price
        self.cashier = cashier
        self.receipt_no = Receipt._receipt_counter
        Receipt._receipt_counter += 1

    def create(self):
        return (
            f"Receipt No : {self.receipt_no}"
            f"Total Price : {self.pricetopay}\n"
            f"Discount Percent : {self.discount_percent}\n"
            f"Total Payable : {self.discount_price}\n"
            f"Balance : {self.paid_amount}\n"
            f"Change : {self.change}\n"
            f"Processed By : {self.cashier} ID : {self.cashier.id}\n"
        )
