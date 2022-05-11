
class LinkedListWithIndex():

    class Node():
        def __init__(self, index, data):
            self.index = index
            self.data = data
            self.next = None
            
    def __init__(self):
        self.head = None
        self.size = 0

    def add_front(self, index, data):
        new_node = self.Node(index, data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def add_back(self, index, data):

        new_node = self.Node(index, data)

        if not self.head:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

        self.size += 1

    def delete(self, value):
        if not self.head:
            raise Exception("Empty list.")

        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
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

    def get_by_index(self, index):
        if not self.head:
            raise Exception("Empty list.")

        current = self.head

        while current:
            if current.index == index:
                return current.data

            current = current.next
            
        return None

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

    def print(self):
        current = self.head

        while current:
            print(f'index: {current.index}, value: {current.data}')
            current = current.next
