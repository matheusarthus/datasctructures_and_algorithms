from algorithms.max_int_heap import MaxIntHeap


def test_extract_max():
    max_int_heap = MaxIntHeap()

    max_int_heap.insert(42)
    max_int_heap.insert(29)
    max_int_heap.insert(18)
    max_int_heap.insert(35)

    max_int_heap.print()

    assert max_int_heap.items.get(0) == 42
    assert max_int_heap.items.get(1) == 35
    assert max_int_heap.items.get(2) == 18
    assert max_int_heap.items.get(3) == 29

    assert max_int_heap.extract_max() == 42
    assert max_int_heap.extract_max() == 35
    assert max_int_heap.extract_max() == 29
    assert max_int_heap.extract_max() == 18

    max_int_heap.print()

def test_extract_max_bigger():
    max_int_heap = MaxIntHeap()

    max_int_heap.insert(42)
    max_int_heap.insert(29)
    max_int_heap.insert(18)
    max_int_heap.insert(14)
    max_int_heap.insert(7)
    max_int_heap.insert(18)
    max_int_heap.insert(12)
    max_int_heap.insert(11)
    max_int_heap.insert(13)

    max_int_heap.print()

    assert max_int_heap.extract_max() == 42
    assert max_int_heap.extract_max() == 29
    assert max_int_heap.extract_max() == 18
    assert max_int_heap.extract_max() == 18
    assert max_int_heap.extract_max() == 14
    assert max_int_heap.extract_max() == 13
    assert max_int_heap.extract_max() == 12
    assert max_int_heap.extract_max() == 11
    assert max_int_heap.extract_max() == 7

    max_int_heap.print()
    