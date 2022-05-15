from datetime import datetime

from algorithms.fibonacci import FibonacciNaive, FibonacciMemoized


def test_naive():
    naive = FibonacciNaive()

    assert naive.fib(0) == 0
    assert naive.fib(1) == 1
    assert naive.fib(2) == 1
    assert naive.fib(3) == 2
    assert naive.fib(4) == 3
    assert naive.fib(5) == 5
    assert naive.fib(6) == 8
    assert naive.fib(7) == 13
    assert naive.fib(8) == 21

def test_memoized():
    memo = FibonacciMemoized()

    assert memo.fib(0) == 0
    assert memo.fib(1) == 1
    assert memo.fib(2) == 1
    assert memo.fib(3) == 2
    assert memo.fib(4) == 3
    assert memo.fib(5) == 5
    assert memo.fib(6) == 8
    assert memo.fib(7) == 13
    assert memo.fib(8) == 21

def test_record_time_naive():
    naive = FibonacciNaive()

    start_datetime = datetime.now()
    naive.fib(30)
    end_datetime = datetime.now()

    print(f'elapsedTime = {end_datetime - start_datetime}')

def test_record_time_memoized():
    memo = FibonacciMemoized()

    start_datetime = datetime.now()
    memo.fib(50)
    end_datetime = datetime.now()

    print(f'elapsedTime = {end_datetime - start_datetime}')
