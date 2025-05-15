class Observer:
    def update(self, message):
        pass


class Logger(Observer):
    def update(self, message):
        print(f"[LOG]: {message}")


class StockAlertSystem(Observer):
    def update(self, message):
        if "low stock" in message:
            print(f"[ALERT]: {message}")


class RecordViewer:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
