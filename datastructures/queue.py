from datastructures.double_linked_list import DoubleLinkedList

class Queue(DoubleLinkedList):

    def add(self, value):
        self.add_back(value)

    def remove(self):
        self.delete(self.head.data)
        