from abc import ABC, abstractmethod


class Donate(ABC):
    def __init__(self):
        self.total = []

    def process_donation(self, amount):
        if self.validate(amount):
            self.store(amount)
            self.custom_action(amount)
        else:
            print("Invalid donation amount.")

    def validate(self, amount):
        return isinstance(amount, (int, float)) and amount > 0

    def store(self, amount):
        self.total.append(amount)
        print(f"Stored donation: ₱{amount}")

    @abstractmethod
    def custom_action(self, amount):
        pass


class OnlineDonation(Donate):
    def custom_action(self, amount):
        print(f"Online receipt emailed for ₱{amount}.")


class FunRun(Donate):
    def custom_action(self, amount):
        if amount >= 1000:
            print("Donor qualifies for free Fun Run T-shirt.")
        else:
            print("Thank you for supporting the Fun Run.")


od = OnlineDonation()
od.process_donation(500)
# Output:
# Stored donation: ₱500
# Online receipt emailed for ₱500.

fr = FunRun()
fr.process_donation(1500)
# Output:
# Stored donation: ₱1500
# Donor qualifies for free Fun Run T-shirt.
