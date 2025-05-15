class Payment:
    def process_payment(self, amount):
        return amount


class Cash(Payment):
    def process_payment(self, amount):
        return amount  # No extra fees


class CreditCard(Payment):
    def process_payment(self, amount):
        return amount * 1.001  # +0.10%
