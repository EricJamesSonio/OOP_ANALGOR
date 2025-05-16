from abc import ABC, abstractmethod

class Order:
    def __init__(self, total_amount):
        self.total_amount = total_amount
        self.state 
        
class OrderState(ABC):
    def __init__(self, order : Order, discount_strategy : 'DiscountStrategy'):
        self.order = order
        self.discount_strategy = discount_strategy
        
    @abstractmethod
    def calculate_price(self):
        pass
    
    @abstractmethod
    def next_state(self):
        pass
    
class Pending(OrderState):
    def __init__(self, order, discount_strategy = 'PendingDiscount'):
        super().__init__(order, discount_strategy)
    def calculate_price(self):
        return super().calculate_price()
    
    def next_state(self):
        return super().next_state()
    
class Processed(OrderState):
    def __init__(self, order, discount_strategy = 'ProcessedDiscount'):
        super().__init__(order, discount_strategy)
    def calculate_price(self):
        return super().calculate_price()
    
    def next_state(self):
        return super().next_state()
    
class Shipped(OrderState):
    def __init__(self, order, discount_strategy = 'ShippedDiscount'):
        super().__init__(order, discount_strategy)
    def calculate_price(self):
        return super().calculate_price()

    def next_state(self):
        return super().next_state()
    
class Delivered(OrderState):
    def __init__(self, order, discount_strategy = 'DeliveredDiscount'):
        super().__init__(order, discount_strategy)
    def calculate_price(self):
        return super().calculate_price()

    def next_state(self):
        return super().next_state()
    
class DiscountStrategy(ABC):
    def apply_discount(self, amount):
        pass
    
class PendingDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.1
    
class ProcessedDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.2
    
class ShippedDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.3
    
class DeliveredDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.4
    

    
