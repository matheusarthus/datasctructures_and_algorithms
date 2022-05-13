from algorithms.binary_search_tree import BinarySearchTree


def test_insert():
    bst = BinarySearchTree()

    bst.insert(5, "e")
    bst.insert(3, "c")
    bst.insert(2, "b")
    bst.insert(4, "d")
    bst.insert(7, "g")
    bst.insert(6, "f")
    bst.insert(8, "h")

    assert bst.find(5) == "e"
    assert bst.find(3) == "c"
    assert bst.find(2) == "b"
    assert bst.find(4) == "d"
    assert bst.find(7) == "g"
    assert bst.find(6) == "f"
    assert bst.find(8) == "h"
    assert not bst.find(99)

    bst.pretty_print()

def test_min_key():
    bst = BinarySearchTree()

    bst.insert(5, "e")
    bst.insert(3, "c")
    bst.insert(2, "b")

    assert bst.find_min_key() == 2

    bst.pretty_print()

def test_delete_no_child():
    bst = BinarySearchTree()

    bst.insert(5, "e")
    bst.insert(3, "c")
    bst.insert(2, "b")
    bst.insert(4, "d")
    bst.insert(7, "g")
    bst.insert(6, "f")
    bst.insert(8, "h")

    bst.pretty_print()

    bst.delete(2)

    assert not bst.find(2)

    bst.pretty_print()

def test_delete_one_child():
    bst = BinarySearchTree()

    bst.insert(5, "e")
    bst.insert(3, "c")
    bst.insert(2, "b")
    bst.insert(4, "d")
    bst.insert(7, "g")
    bst.insert(8, "h")

    bst.pretty_print()

    bst.delete(7)

    assert not bst.find(7)

    bst.pretty_print()

def test_delete_two_children():
    bst = BinarySearchTree()

    bst.insert(5, "e")
    bst.insert(3, "c")
    bst.insert(2, "b")
    bst.insert(4, "d")
    bst.insert(7, "g")
    bst.insert(6, "f")
    bst.insert(8, "h")

    bst.pretty_print()

    bst.delete(7)

    assert not bst.find(7)

    bst.pretty_print()

def test_check_bst1():
    bst = BinarySearchTree()

    bst.insert(5, "e")
    bst.insert(3, "c")
    bst.insert(2, "b")
    bst.insert(4, "d")
    bst.insert(7, "g")
    bst.insert(6, "f")
    bst.insert(8, "h")

    assert bst.check_bst(bst.root)
    