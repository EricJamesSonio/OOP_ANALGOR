class ProductBase:
    def __init__(self, name, code, price, supplier, quantity, unit, expiration_date):
        self.name = name
        self.code = code
        self.price = price
        self.supplier = supplier
        self.quantity = quantity
        self.unit = unit
        self.expiration_date = expiration_date

    def get_details(self):
        return (
            f"Name: {self.name}, Code: {self.code}, Price: {self.price}, "
            f"Supplier: {self.supplier}, Quantity: {self.quantity} {self.unit}, "
            f"Expiration: {self.expiration_date}"
        )
