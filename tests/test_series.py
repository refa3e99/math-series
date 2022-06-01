import pytest

from series.series import Fibonacci, lucas, sum_series

#fibonacci tests
def test_fib_zero():
    actual = Fibonacci(0)
    expected = 0

    assert actual == expected

def test_fib_one():
    actual = Fibonacci(1)
    expected = 1

    assert actual == expected

def test_fib_two():
    actual = Fibonacci(2)
    expected = 1
    assert actual == expected

def test_fib_three():
    actual = Fibonacci(3)
    expected = 2

    assert actual == expected

def test_fib_four():
    actual = Fibonacci(4)
    expected = 3

    assert actual == expected

def test_fib_minusone():
    actual = Fibonacci(-1)
    expected = 'incorrect input'

    assert actual == expected


#lucas tests
def test_luc_zero():
    actual = lucas(0)
    expected = 2

    assert actual == expected

def test_luc_one():
    actual = lucas(1)
    expected = 1

    assert actual == expected

def test_luc_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_luc_three():
    actual = lucas(3)
    expected = 4

    assert actual == expected

def test_luc_four():
    actual = lucas(4)
    expected = 7

    assert actual == expected

def test_luc_minusone():
    actual = lucas(-1)
    expected = 'incorrect input'

    assert actual == expected

#sum_series tests
def test_sum_series_seven():
    actual = sum_series(7)
    expected = 13
    assert actual == expected

def test_sum_series_four():
    actual = sum_series(4,2,3)
    expected = 13
    assert actual == expected

def test_sum_series_zero():
    actual = sum_series(0,7,8)
    expected = 7
    assert actual == expected




