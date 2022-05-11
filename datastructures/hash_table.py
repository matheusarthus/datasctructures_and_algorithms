from datastructures.dynamic_array import DynamicArray
from datastructures.linked_list_with_index import LinkedListWithIndex


class HashTable():
    INITIAL_SIZE = 16
    
    def __init__(self) -> None:
        self.data = DynamicArray(self.INITIAL_SIZE)

    def put(self, key, value):
        
        index = self._get_index(key)

        if not self.data.get(index):
            new_row = LinkedListWithIndex()
            new_row.add_front(key, value)
            self.data.set(index, new_row)
        else:
            row = self.data.get(index)
            row.add_front(key, value)

    def get(self, key):

        index = self._get_index(key)

        row = self.data.get(index)

        return row.get_by_index(key) if row else None


    def _get_index(self, key: str):
        hash_code = key.__hash__()

        index = (hash_code & 0x7fffffff) % self.INITIAL_SIZE

        #if key == "John Smith" or key == "Sandra Dee" or key == "Tim Lee":
        #    index = 4

        return index
        