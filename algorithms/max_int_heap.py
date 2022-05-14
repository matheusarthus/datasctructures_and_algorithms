from datastructures.dynamic_array import DynamicArray


class MaxIntHeap():
    
    def __init__(self) -> None:
        self.items = DynamicArray(20)

    def left_child_index(self, parent_index) -> int:
        return int(2 * parent_index + 1)

    def right_child_index(self, parent_index) -> int:
        return int(2 * parent_index + 2)

    def parent_index(self, child_index) -> int:
        return int((child_index - 1) / 2)

    def has_left_child(self, index) -> bool:
        return self.left_child_index(index) < self.items.size

    def has_right_child(self, index) -> bool:
        return self.right_child_index(index) < self.items.size

    def has_parent(self, index) -> bool:
        return self.parent_index(index) >= 0

    def left_child(self, index):
        return self.items.get(self.left_child_index(index))

    def right_child(self, index):
        return self.items.get(self.right_child_index(index))

    def parent(self, index):
        return self.items.get(self.parent_index(index))

    def insert(self, item):
        self.items.add(item)
        self.heapify_up()

    def heapify_up(self):
        index = self.items.size - 1

        while self.has_parent(index) and self.parent(index) < self.items.get(index):
            self.swap(self.parent_index(index), index)
            index = self.parent_index(index)

    def extract_max(self):
        if self.items.size == 0:
            raise Exception("Não há itens.")

        item = self.items.get(0)
        self.items.set(0, self.items.get(self.items.size - 1))
        self.items.delete(self.items.size - 1)
        self.heapify_down()

        return item

    def heapify_down(self):
        index = 0

        while self.has_left_child(index):
            larger_child_index = self.left_child_index(index)
            
            if self.has_right_child(index) and self.right_child(index) > self.left_child(index):
                larger_child_index = self.right_child_index(index)

            if self.items.get(index) > self.items.get(larger_child_index):
                break
            else:
                self.swap(index, larger_child_index)

            index = larger_child_index

    def swap(self, index_one, index_two):
        temp = self.items.get(index_one)
        self.items.set(index_one, self.items.get(index_two))
        self.items.set(index_two, temp)

    def print(self):
        print(" ")
        i = 0
        for item in self.items.data:
            print(f'{i} ["{item}"]')
            i += 1