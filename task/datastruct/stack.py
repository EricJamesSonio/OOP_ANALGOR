class Node:
    def __init__(self, number):
        self.number = number
        self.next = None


class Stack:
    def __init__(self, max=10):
        self.top = None
        self.cursor = 0
        self.max = max

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return self.cursor == self.max

    def push(self, node):
        if self.is_empty():
            new_node = Node(node)
            self.top = new_node
