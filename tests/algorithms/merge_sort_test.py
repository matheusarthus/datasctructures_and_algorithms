from algorithms.merge_sort import MergeSort


def test_sort():
    merge_sort = MergeSort()
    array = [4, 7, 14, 1, 3, 9, 17]

    L = 0
    R = len(array) - 1

    merge_sort.sort(array, L, R)

    assert array[0] == 1
    assert array[1] == 3
    assert array[2] == 4
    assert array[3] == 7
    assert array[4] == 9
    assert array[5] == 14
    assert array[6] == 17

    print('\nSorted array')
    merge_sort.print_array(array)
    