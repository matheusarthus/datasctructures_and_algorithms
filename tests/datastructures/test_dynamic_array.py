from datastructures.dynamic_array import DynamicArray


def test_get_and_set():
    array = DynamicArray(10)
    array.set(0, "a")

    assert array.get(0) == "a"

def test_add():
    array = DynamicArray(10)

    array.add("a")
    array.add("b")
    array.add("c")

    assert array.size   == 3
    assert array.get(0) == "a"
    assert array.get(1) == "b"
    assert array.get(2) == "c"

def test_insert():
    array = DynamicArray(10)

    array.add("a")
    array.add("b")
    array.add("c")

    array.insert(1, "d")

    assert array.size   == 4
    assert array.get(0) == "a"
    assert array.get(1) == "d"
    assert array.get(2) == "b"
    assert array.get(3) == "c"

def test_delete_first():
    array = DynamicArray(10)

    array.add("a")
    array.add("b")
    array.add("c")

    array.delete(0)

    assert array.size   == 2
    assert array.get(0) == "b"
    assert array.get(1) == "c"
    assert array.get(2) == None

def test_delete_middle():
    array = DynamicArray(10)

    array.add("a")
    array.add("b")
    array.add("c")

    array.delete(1)

    assert array.size   == 2
    assert array.get(0) == "a"
    assert array.get(1) == "c"
    assert array.get(2) == None

def test_delete_last():
    array = DynamicArray(10)

    array.add("a")
    array.add("b")
    array.add("c")

    array.delete(2)

    assert array.size   == 2
    assert array.get(0) == "a"
    assert array.get(1) == "b"
    assert array.get(2) == None

def test_is_empty():
    array = DynamicArray(10)

    assert array.is_empty()
    array.add("a")
    assert not array.is_empty()

def test_contains():
    array = DynamicArray(10)

    assert not array.contains("a")
    array.add("a")
    assert array.contains("a")
    array.add("b")
    array.add("b")
    array.add("c")
    assert array.contains("b")
    assert array.contains("c")
    array.delete(3)
    assert not array.contains("c")
    array.delete(2)
    assert array.contains("b")
    array.delete(1)
    assert not array.contains("b")
    array.delete(0)
    assert not array.contains("a")