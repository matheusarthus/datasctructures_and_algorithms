from datastructures.linked_list import LinkedList

class Stack(LinkedList):
    
    def push(self, value):
        self.add_front(value)

    def pop(self):
        current = self.head

        self.delete(current.data)

        return current.data
