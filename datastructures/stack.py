from datastructures.linked_list import LinkedList

class Stack():
    
    def __init__(self):
        self.stack = LinkedList()
        self.size = 0
        self.peek = None

    def push(self, value):
        self.stack.add_front(value)
        self.size = self.stack.size
        self.peek = value

    def pop(self):
        if not self.stack.head:
            raise Exception("Empty list.")

        current = self.stack.head

        self.stack.delete(current.data)
        self.peek = self.stack.head.data if self.stack.head else None
        self.size = self.stack.size

        return current.data

    def is_empty(self):
        return self.size == 0