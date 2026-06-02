import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(10, 5) == 50
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 5) == 2.0
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="0で割ることはできません"):
        divide(10, 0)
