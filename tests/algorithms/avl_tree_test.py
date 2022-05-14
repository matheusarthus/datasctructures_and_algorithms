from algorithms.avl_tree import AVLTree


def test_left_left_on_insert():
    avl_tree = AVLTree()

    avl_tree.insert(30, "a")
    avl_tree.insert(20, "b")
    avl_tree.insert(10, "c")

    avl_tree.print_in_order_traversal()

    assert avl_tree.root.key == 20

def test_right_right_on_insert():
    avl_tree = AVLTree()

    avl_tree.insert(30, "a")
    avl_tree.insert(40, "b")
    avl_tree.insert(50, "c")

    avl_tree.print_in_order_traversal()

    assert avl_tree.root.key == 40

def test_left_right_on_insert():
    avl_tree = AVLTree()

    avl_tree.insert(30, "a")
    avl_tree.insert(20, "b")
    avl_tree.insert(25, "c")

    avl_tree.print_in_order_traversal()

    assert avl_tree.root.key == 25

def test_right_left_on_insert():
    avl_tree = AVLTree()

    avl_tree.insert(30, "a")
    avl_tree.insert(40, "b")
    avl_tree.insert(35, "c")

    avl_tree.print_in_order_traversal()

    assert avl_tree.root.key == 35

def test_left_left_on_delete():
    avl_tree = AVLTree()

    avl_tree.insert(30, "a")
    avl_tree.insert(40, "d")
    avl_tree.insert(20, "b")
    avl_tree.insert(10, "c")

    avl_tree.print_in_order_traversal()

    avl_tree.delete(40)

    avl_tree.print_in_order_traversal()

    assert avl_tree.root.key == 20

def test_right_right_on_delete():
    avl_tree = AVLTree()

    avl_tree.insert(30, "a")
    avl_tree.insert(20, "d")
    avl_tree.insert(40, "b")
    avl_tree.insert(50, "c")

    avl_tree.print_in_order_traversal()

    avl_tree.delete(20)

    avl_tree.print_in_order_traversal()

    assert avl_tree.root.key == 40

def test_left_right_on_delete():
    avl_tree = AVLTree()

    avl_tree.insert(30, "a")
    avl_tree.insert(40, "d")
    avl_tree.insert(20, "b")
    avl_tree.insert(25, "c")

    avl_tree.print_in_order_traversal()

    avl_tree.delete(40)

    avl_tree.print_in_order_traversal()

    assert avl_tree.root.key == 25

def test_right_left_on_delete():
    avl_tree = AVLTree()

    avl_tree.insert(30, "a")
    avl_tree.insert(20, "d")
    avl_tree.insert(40, "b")
    avl_tree.insert(35, "c")

    avl_tree.print_in_order_traversal()

    avl_tree.delete(20)

    avl_tree.print_in_order_traversal()

    assert avl_tree.root.key == 35
