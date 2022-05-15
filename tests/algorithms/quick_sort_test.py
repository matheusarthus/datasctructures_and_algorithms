from algorithms.quick_sort import QuickSort


def test_sort():
    quick_sort = QuickSort()

    array = [15, 3, 2, 1, 9, 5, 7, 8, 6]

    sorted = quick_sort.sort(array )

    assert sorted[0] == 1
    assert sorted[1] == 2
    assert sorted[2] == 3
    assert sorted[3] == 5
    assert sorted[4] == 6
    assert sorted[5] == 7
    assert sorted[6] == 8
    assert sorted[7] == 9
    assert sorted[8] == 15
