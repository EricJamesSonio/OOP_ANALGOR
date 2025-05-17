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
        return f"{self.code} - {self.name} | Qty: {self.quantity} {self.unit} | Price: {self.price} | Supplier: {self.supplier} | Exp: {self.expiration_date}"


    def to_dict(self):
        return {
            "name": self.name,
            "code": self.code,
            "price": self.price,
            "supplier": self.supplier,
            "quantity": self.quantity,
            "unit": self.unit,
            "expiration_date": self.expiration_date,
        }

    @staticmethod
    def from_dict(data):
        return ProductBase(
            name=data["name"],
            code=data["code"],
            price=data["price"],
            supplier=data["supplier"],
            quantity=data["quantity"],
            unit=data["unit"],
            expiration_date=data["expiration_date"],
        )
