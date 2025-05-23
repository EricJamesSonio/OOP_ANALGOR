from abc import ABC, abstractmethod

class Observer(ABC):
    def __init__(self):
        self.records = []
        
    @abstractmethod
    def update(self, message):
        pass
    
class Logger(Observer):
    def update(self, message):
        if message["action"] == "add_item":
            item = message["item"]
            quantity = message["quantity"]
            record = f"Added Item : {item.name} Quantity : {quantity}"
            self.records.append(record)
        elif message["action"] == "removed_item":
            item = message["item"]
            quantity = message["quantity"]
            record = f"Removed Item : {item.name} Quantity : {quantity}"
            self.records.append(record)
        else:
            return None
    
class StockAlertSystem(Observer):
    def update(self, message):
        if message["action"] == "add_stock":
            item = message["item"]
            total = message["total"]
            quantity = message["quantity"]
            record = f"Add Stock : {item.name} Added Qtty : {quantity} Total : {total}"
            self.records.append(record)
        elif message["action"] == "update_stock":
            item = message["item"]
            update = message["update"]
            quantity = message["quantity"]
            record = f"Add Stock : {item.name} difference {update} Total : {quantity}"
            self.records.append(record)
        else:
            return None
    
class ObserverViewer:
    def __init__(self, observer : Observer):
        self.observer = observer
        
    def display_records(self):
        for record in self.observer.records:
            print(record)
            
