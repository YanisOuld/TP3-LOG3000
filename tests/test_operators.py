"""Unit tests targeting the arithmetic helper functions in `operators.py`."""

import pytest

from operators import add, subtract, multiply, divide


def test_add_returns_sum():
    """add should combine both operands into a summed value."""

    assert add(5, 7) == pytest.approx(12)


def test_subtract_returns_difference():
    """subtract should remove the second operand from the first one."""

    assert subtract(10, 4) == pytest.approx(6)


def test_multiply_returns_product():
    """multiply should scale the first operand by the second operand."""

    assert multiply(3, 4) == pytest.approx(12)


def test_divide_returns_true_division():
    """divide should support fractional results rather than floor division."""

    assert divide(5, 2) == pytest.approx(2.5)

