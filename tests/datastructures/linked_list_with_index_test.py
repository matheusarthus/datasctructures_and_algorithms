from datastructures.linked_list_with_index import LinkedListWithIndex


def test_get_by_index():
    linked_list = LinkedListWithIndex()

    linked_list.add_front(99, 1)
    linked_list.add_front(100, 2)
    linked_list.add_front(101, 3)

    linked_list.print()

    assert linked_list.get_by_index(99)
    assert linked_list.get_by_index(100)
    assert linked_list.get_by_index(101)
