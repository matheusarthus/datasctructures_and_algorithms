from datastructures.dynamic_array import DynamicArray


class FibonacciNaive():
    
    def fib(self, value):
        if value <= 0:
            return 0
        elif value == 1:
            return 1
        else:
            return self.fib(value-1) + self.fib(value-2)

class FibonacciMemoized():
    
    def __init__(self) -> None:
        self.memo = DynamicArray(1001)

    def fib(self, value):
        if value <= 0:
            return 0
        elif value == 1:
            return 1
        elif not self.memo.get(value):
            self.memo.set(value, self.fib(value-1) + self.fib(value-2))
        
        return self.memo.get(value)
