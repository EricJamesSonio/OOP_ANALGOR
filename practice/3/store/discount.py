class Discount:
    def apply(self, total):
        return total


class NoDiscount(Discount):
    def apply(self, total):
        return total


class PWDDiscount(Discount):
    def apply(self, total):
        return total * 0.90


class SeniorDiscount(Discount):
    def apply(self, total):
        return total * 0.85
