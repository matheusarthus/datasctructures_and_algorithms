

class BubbleSort():
    
    def sort(self, array):
        print("")
        print(array)
        for i in range(len(array) - 1):
            for j in range(len(array) - i - 1):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        print(array)
        return array