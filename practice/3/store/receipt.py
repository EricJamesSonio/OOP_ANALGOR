class Receipt:
    def generate(self, items, total, payment_type):
        print("----- RECEIPT -----")
        for item in items:
            print(f"{item.name} x {item.quantity} = {item.price * item.quantity}")
        print(f"Total: {total}")
        print(f"Paid via: {payment_type}")
        print("-------------------")
