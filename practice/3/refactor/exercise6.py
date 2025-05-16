from abc import ABC, abstractmethod


# ---- Strategies ----
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.05

class GovernmentDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.1

class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return 0


class TaxStrategy(ABC):
    @abstractmethod
    def apply_tax(self, price):
        pass

class RegularTax(TaxStrategy):
    def apply_tax(self, price):
        return price * 0.1

class VipTax(TaxStrategy):
    def apply_tax(self, price):
        return price * 0.08

class NoTax(TaxStrategy):
    def apply_tax(self, price):
        return 0


# ---- Customer Types ----
class Customer:
    def __init__(self, discount_strategy: DiscountStrategy, tax_strategy: TaxStrategy):
        self.discount_strategy = discount_strategy
        self.tax_strategy = tax_strategy



class RegularCustomer(Customer):
    def __init__(self):
        super().__init__(NoDiscount(), RegularTax())


class VIPCustomer(Customer):
    def __init__(self):
        super().__init__(VIPDiscount(), VipTax())


class GovernmentCustomer(Customer):
    def __init__(self):
        super().__init__(GovernmentDiscount(), NoTax())


# ---- Formatters ----
class TextStrategy(ABC):
    @abstractmethod
    def write(self, content):
        pass

class HTML(TextStrategy):
    def write(self, content):
        return f"<html><body>{content}</body></html>"

class Text(TextStrategy):
    def write(self, content):
        return content

class Json(TextStrategy):
    def write(self, content):
        return {"invoice": content}


# ---- Invoice Class ----
class Invoice:
    def __init__(self, customer: Customer, amount: float, formatter: TextStrategy):
        self.customer = customer
        self.amount = amount
        self.formatter = formatter

    def generate_invoice(self):
        calculator = InvoiceCalculator(self.customer, self.amount)
        summary = calculator.calculate()

        content = (
            f"Amount: ₱{summary['amount']:.2f}\n"
            f"Tax: ₱{summary['tax']:.2f}\n"
            f"Discount: ₱{summary['discount']:.2f}\n"
            f"Total Payable: ₱{summary['total']:.2f}"
        )
        return content

    def send_invoice(self):
        return self.formatter.write(self.generate_invoice())

    
class InvoiceCalculator:
    def __init__(self, customer: Customer, amount: float):
        self.customer = customer
        self.amount = amount

    def calculate(self):
        discount = self.customer.discount_strategy.apply_discount(self.amount)
        tax = self.customer.tax_strategy.apply_tax(self.amount)
        total = self.amount + tax - discount
        return {
            "amount": self.amount,
            "tax": tax,
            "discount": discount,
            "total": total
        }

