from typing import List, Dict
from inventory import Observer, Logger


class Table:
    def __init__(self, table_no, capacity):
        self.table_no = table_no
        self.capacity = capacity
        self.is_available = True

    def __str__(self):
        return f"Table No : {self.table_no}, Capacity : {self.capacity}, Is Available : {self.is_available}"


class Table_Management:
    def __init__(self):
        self.tables: Dict[int, Table] = {
            1: Table(1, 4),
            2: Table(2, 6),
            3: Table(3, 8),
            4: Table(4, 5),
            5: Table(5, 2),
            6: Table(6, 4),
            7: Table(7, 4),
            8: Table(8, 4),
            9: Table(9, 5),
            10: Table(10, 4),
        }
        self.logger = Logger()
        self.observers: List["Observer"] = [self.logger]

    def display_table(self):
        for table in self.tables.values():
            print(table)

    def reserve_table(self, table_no: int):
        if table_no in self.tables and self.tables[table_no].is_available:
            self.tables[table_no].is_available = False

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


table = Table_Management()
table.display_table()
