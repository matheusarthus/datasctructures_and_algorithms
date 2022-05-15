from algorithms.bubble_sort import BubbleSort


def test_sort():
    bubble_sort = BubbleSort()
    array = [5, 1, 4, 2, 8]

    sorted = bubble_sort.sort(array)

    assert sorted[0] == 1
    assert sorted[1] == 2
    assert sorted[2] == 4
    assert sorted[3] == 5
    assert sorted[4] == 8
