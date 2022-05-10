from datastructures.stack import Stack


def test_push():
    stack = Stack()

    stack.push(15)
    stack.push(25)
    stack.push(75)

    assert stack.size == 3
    assert stack.peek == 75
    assert not stack.is_empty()

def test_pop():
    stack = Stack()

    stack.push(15)
    stack.push(25)
    stack.pop()
    stack.push(35)
    stack.pop()

    assert stack.peek == 15
    assert stack.size == 1
    assert not stack.is_empty()
    assert stack.pop() == 15
