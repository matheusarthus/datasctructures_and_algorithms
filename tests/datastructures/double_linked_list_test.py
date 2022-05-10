from datastructures.double_linked_list import DoubleLinkedList


def test_get_first():
    linked_list = DoubleLinkedList()

    linked_list.add_front(1)

    assert linked_list.get_first() == 1

def test_get_last():
    linked_list = DoubleLinkedList()

    linked_list.add_front(1)
    linked_list.add_front(2)
    linked_list.add_front(3)

    assert linked_list.get_last() == 1

def test_add_front():
    linked_list = DoubleLinkedList()

    linked_list.add_front(1)
    linked_list.add_front(2)
    linked_list.add_front(3)

    assert linked_list.get_first() == 3
    assert linked_list.get_last()  == 1

def test_add_back():
    linked_list = DoubleLinkedList()

    linked_list.add_back(1)
    linked_list.add_back(2)
    linked_list.add_back(3)

    assert linked_list.get_first() == 1
    assert linked_list.get_last()  == 3

def test_size():
    linked_list = DoubleLinkedList()

    assert linked_list.size == 0
    linked_list.add_back(1)
    assert linked_list.size == 1
    linked_list.add_back(2)
    assert linked_list.size == 2

def test_clear():
    linked_list = DoubleLinkedList()

    linked_list.add_back(1)
    linked_list.add_back(2)
    linked_list.add_back(3)

    linked_list.clear()

    assert linked_list.size == 0

def test_delete():
    linked_list = DoubleLinkedList()

    linked_list.add_back(1)
    linked_list.add_back(2)
    linked_list.add_back(3)

    linked_list.delete(2)

    assert linked_list.size == 2
    assert linked_list.get_first() == 1
    assert linked_list.get_last()  == 3

def test_delete_last_value():
    linked_list = DoubleLinkedList()

    linked_list.add_back(1)
    linked_list.add_back(2)
    linked_list.add_back(3)
    linked_list.add_back(4)

    linked_list.delete(4)

    assert linked_list.size == 3
    assert linked_list.get_first() == 1
    assert linked_list.get_last()  == 3
