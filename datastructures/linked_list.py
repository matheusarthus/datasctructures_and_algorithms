
class LinkedList():

    class Node():
        def __init__(self, data):
            self.data = data
            self.next = None
            
    
    def __init__(self):
        self.head = None
        self.size = 0
        self.peek = None

    def add_front(self, data):

        new_node = self.Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1
        self.peek = new_node.data

    def add_back(self, data):

        new_node = self.Node(data)

        if not self.head:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

        self.size += 1
        self.peek = self.head.data

    def delete(self, value):
        if not self.head:
            raise Exception("Empty list.")

        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
            self.peek = self.head.data if self.head else None
            return

        current = self.head
        next    = self.head.next

        while next:
            if next.data == value:
                current.next = next.next
                self.size -= 1
                return
                
            current = current.next
            next    = next.next

        raise Exception("Value not found.")

    def get_first(self):
        if not self.head:
            raise Exception("Empty list.")
            
        return self.head.data

    def get_last(self):
        if not self.head:
            raise Exception("Empty list.")

        current = self.head

        while current.next:
            current = current.next

        return current.data

    def clear(self):
        self.head = None
        self.size = 0
        self.peek = None

    def is_empty(self):
        return self.size == 0

    def print(self):
        current = self.head

        while current:
            print(f'data: {current.data}, next: {current.next}')
            current = current.next