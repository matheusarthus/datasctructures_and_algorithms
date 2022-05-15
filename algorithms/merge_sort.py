

class MergeSort():
    
    def sort(self, array, L, R):
        print(f'\nsplitting L R: {L} {R}')
        
        if  L < R:
            M = int((L + R)/2)

            self.sort(array, L, M)
            self.sort(array, M+1, R)

            self.merge(array, L, M, R)

    def merge(self, array, L, M, R):
        print(f'\nmerge L M R: {L} {M} {R}')

        n1 = M - L + 1
        n2 = R - M
        
        l = array[L:M+1]
        r = array[M+1:R+1]

        i = 0
        j = 0

        k = L
        while i < n1 and j < n2:
            if l[i] <= r[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = r[j]
                j += 1
            k += 1

        while i < n1:
            array[k] = l[i]
            i += 1
            k += 1

        while j < n2:
            array[k] = r[j]
            j += 1
            k += 1

        print('\nAfter merge')
        self.print_array(array)

    def print_array(self, array):
        for item in array:
            print(f'{item} ')