

class DynamicArray(): 
    def __init__(self, initial_capacity):
        self.capacity = initial_capacity
        self.data = [None for i in range(initial_capacity)]
        self.size = 0

    def set(self, index, value):
        if index > self.capacity - 1:
            self._resize()

        self.data[index] = value

    def get(self, index):
        return self.data[index]

    def add(self, value):
        if self.size == self.capacity:
            self._resize_array()

        self.data[self.size] = value
        self.size += 1 

    def insert(self, index, value):
        if self.size == self.capacity:
            self._resize_array()

        for i in reversed(range(index, self.size+1)):
            self.data[i] = self.data[i-1]

        self.data[index] = value
        self.size += 1
            
    def delete(self, index):
        print(self.data)
        for i in range(index, self.size+1):
            print(i)
            self.data[i] = self.data[i+1]
            print(self.data)
            
        self.size -= 1

    def is_empty(self):
        return self.size == 0

    def contains(self, value):
        for x in self.data:
            if x == value:
                return True
        return False

    def _resize(self):
        new_capacity = self.capacity * 2
        new_data = [None for i in range(new_capacity)]

        for index in range(self.capacity):
            new_data[index] = self.data[index]
        
        self.capacity = new_capacity
        self.data = new_data
