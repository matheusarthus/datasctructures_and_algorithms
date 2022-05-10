
class DoubleLinkedList():

    class Node():
        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None
            
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_front(self, data):

        new_node = self.Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def add_back(self, data):

        new_node = self.Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

        self.size += 1

    def delete(self, value):
        if not self.head:
            raise Exception("Empty list.")

        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
            return

        if self.tail.data == value:
            self.tail = self.tail.previous
            self.size -= 1
            return

        current = self.head
        next    = self.head.next

        while next:
            if next.data == value:
                current.next = next.next
                next.next.previous = current
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

        return self.tail.data

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print(self):
        current = self.head

        while current:
            print(f'data: {current.data}, next: {current.next}, previous: {current.previous}')
            current = current.next