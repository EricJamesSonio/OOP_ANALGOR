from typing import List


class Table:
    def __init__(self, table_no, capacity):
        self.capacity = capacity
        self.table_no = table_no
        self.available = True


class Table_Management:
    def __init__(self):
        self.tables: List["Table"] = []

    def find_table(self, table_no):
        for table in self.tables:
            if table.table_no == table_no and table.available:
                return table
        return None

    def assign_table(self, table_no, numguest):
        available_table = self.find_table(table_no)
        if available_table and available_table.capacity >= numguest:
            available_table.available = False

    def vacant_table(self, table_no):
        table = self.find_table(table_no)
        if table and not table.available:
            table.available = True
        else:
            return None
