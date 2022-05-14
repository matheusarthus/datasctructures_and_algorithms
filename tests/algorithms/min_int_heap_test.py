from algorithms.min_int_heap import MinIntHeap


def test_insert():
    min_int_heap = MinIntHeap()

    min_int_heap.insert(6)
    min_int_heap.insert(5)
    min_int_heap.insert(4)
    min_int_heap.insert(3)
    min_int_heap.insert(2)
    min_int_heap.insert(1)

    min_int_heap.print()

    assert min_int_heap.items.get(0) == 1
    assert min_int_heap.items.get(1) == 3
    assert min_int_heap.items.get(2) == 2
    assert min_int_heap.items.get(3) == 6
    assert min_int_heap.items.get(4) == 4
    assert min_int_heap.items.get(5) == 5

def test_extract_min():
    min_int_heap = MinIntHeap()

    min_int_heap.insert(6)
    min_int_heap.insert(5)
    min_int_heap.insert(4)
    min_int_heap.insert(3)
    min_int_heap.insert(2)
    min_int_heap.insert(1)

    min_int_heap.print()

    assert min_int_heap.extract_min() == 1
    assert min_int_heap.extract_min() == 2
    assert min_int_heap.extract_min() == 3
    assert min_int_heap.extract_min() == 4
    assert min_int_heap.extract_min() == 5
    assert min_int_heap.extract_min() == 6

    min_int_heap.print()
    