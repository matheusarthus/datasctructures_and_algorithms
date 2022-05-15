

class QuickSort():
    
    def sort(self, array):
        self.quick_sort(array, 0, len(array) - 1)

        return array

    def quick_sort(self, array, left, right):
        if left >= right:
            return

        pivot = array[int((left + right)/2)]

        index = self.partition(array, left, right, pivot)

        self.quick_sort(array, left, index - 1)
        self.quick_sort(array, index, right)

    def partition(self, array, left, right, pivot):
        while left <= right:

            while array[left] < pivot:
                left += 1

            while array[right] > pivot:
                right -= 1

            if left <= right:
                self.swap(array, left, right)
                left += 1
                right -= 1

        return left

    def swap(self, array, left, right):
        temp = array[left]
        array[left] = array[right]
        array[right] = temp

    def pretty_print(self, array):
        for item in array:
            print(item)