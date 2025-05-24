from store import Store
from cashier import Cashier, OrderItem, Order


class FoodMenu:
    def __init__(self, store: Store):
        self.store = store
        self.store.choose_inventory("food")
        self.cart = []

    def display_items(self):
        self.store.display_items()

    def choose_category(self, choice):
        if choice == "1":
            self.store.display_main_course()
        elif choice == "2":
            self.store.display_dessert()
        else:
            return None

    def category_menu(self):
        print("<-- Choose Category -->")
        print("[1]. Main Course")
        print("[2]. Dessert")
        choice = input("Enter : ")
        self.choose_category(choice)

    def check_out(self):
        for item in self.cart:
            pass
