# Extract Method
# Instead of writing all the function inside. Create a new method that can be reuse in other methods!
"Take a fragment of code that can stand on its own and turn it into a separate method,"
" giving it a clear, descriptive name."


class Inventory:
    def __init__(self):
        self.items = []

    def find_item(self, code):  # Helper Method !!
        for item in self.items:
            if item.code == code:
                return item
        return None

    def add_item(self, item):
        product = self.find_item(item.code)  # Used Here!
        if product:
            product.quantity += item.quantity
        else:
            self.items.append(item)

    def remove_item(self, code):
        product = self.find_item(code)  # Used Here!
        if product:
            self.items.remove(product)
        else:
            return None
