# -------------------------------
# Product Class (Independent)
# -------------------------------
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity


# -------------------------------
# Inventory (Aggregation of Products)
# -------------------------------
class Inventory:
    def __init__(self):
        self.products = {}  # key: product_id, value: Product instance

    def add_product(self, product):
        self.products[product.product_id] = product

    def get_product(self, product_id):
        return self.products.get(product_id)

    def update_stock(self, product_id, quantity):
        product = self.get_product(product_id)
        if product:
            product.update_stock(quantity)


# -------------------------------
# Cart (Aggregation of Products)
# -------------------------------
class Cart:
    def __init__(self):
        self.items = {}  # key: product_id, value: (Product, quantity)

    def add_item(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id] = (
                product,
                self.items[product.product_id][1] + quantity,
            )
        else:
            self.items[product.product_id] = (product, quantity)

    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def calculate_total(self):
        return sum(product.price * qty for product, qty in self.items.values())


# -------------------------------
# OrderProcessor (Depends on Cart and Inventory)
# -------------------------------
class OrderProcessor:
    def process_order(self, cart, inventory):
        # Check stock and deduct
        for product_id, (product, quantity) in cart.items.items():
            stock_product = inventory.get_product(product_id)
            if stock_product and stock_product.stock >= quantity:
                stock_product.update_stock(-quantity)
            else:
                raise ValueError(f"Not enough stock for product: {product.name}")
        return cart.calculate_total()


# -------------------------------
# Store (Composes Inventory, Aggregates Cart)
# -------------------------------
class Store:
    def __init__(self):
        self.inventory = Inventory()  # Composition: Store owns Inventory

    def start_cart(self):
        return Cart()  # Aggregation: Cart is used but not owned permanently

    def checkout(self, cart):
        processor = OrderProcessor()
        total = processor.process_order(cart, self.inventory)
        return total
