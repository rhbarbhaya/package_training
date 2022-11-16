import pytest
from package_training.calculator import (
    add,
    sub,
    multiply,
    divide,
)


@pytest.mark.parametrize(
    "input1, input2, output",
    [
        (2, 3, 5),
        (0, -2, -2),
        (-1, -2, -3),
        (-1, 1, 0),
        (100, 798, 898),
        (10.0, 79.8, 89.8),
        (79.9123, 1283.19283, 1363.10513),
    ]
)
def test_add(input1, input2, output):
    assert add(input1, input2) == output


@pytest.mark.parametrize(
    "input1, input2, output",
    [
        (2, 3, -1),
        (0, -2, 2),
        (-1, -2, 1),
        (-1, 1, -2),
        (100, 798, -698),
        (10.0, 79.8, -69.8),
        (79.9123, 1283.19283, -1203.28053),
    ]
)
def test_sub(input1, input2, output):
    assert sub(input1, input2) == output


@pytest.mark.parametrize(
    "input1, input2, output",
    [
        (2, 3, 0.666666666666667),
        (0, -2, 0),
        (-1, -2, 0.5),
        (-1, 1, -1),
        (100, 798, 0.12531328320802),
        (192, 10, 19.2),
        (10.0, 79.8, 0.12531328320802),
        (79.9123, 1283.19283, 0.062276142861553),
    ]
)
def test_divide(input1, input2, output):
    assert divide(input1, input2) == pytest.approx(output)


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_divide_test():
    divide(1, 0)


@pytest.mark.parametrize(
    "input1, input2, output",
    [
        (2, 3, 6),
        (0, -2, 0),
        (-1, -2, 2),
        (-1, 1, -1),
        (100, 798, 79800),
        (192, 10, 1920),
        (10.0, 79.8, 798),
        (79.9123, 1283.19283, 102542.890388809),
    ]
)
def test_multiply(input1, input2, output):
    assert multiply(input1, input2) == pytest.approx(output)
