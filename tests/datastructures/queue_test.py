from datastructures.queue import Queue


def test_add():
    queue = Queue()

    queue.add(5)
    queue.add(2)
    queue.add(21)

    assert queue.peek == 5

def test_remove():
    queue = Queue()

    queue.add(8)
    queue.add(72)
    queue.add(11)
    queue.remove()
    queue.add(15)
    queue.add(35)
    queue.remove()

    assert queue.peek == 11

def test_is_empty():
    queue = Queue()

    queue.add(8)
    queue.remove()

    assert queue.is_empty()
