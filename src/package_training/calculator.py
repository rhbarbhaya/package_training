"""Simple mathematical functions to test the packaging functions."""


def add(
    number1: int | float = 0,
    number2: int | float = 0,
) -> int | float:
    """Adds two numbers and returns the mathematical number of two numbers

    :param number1: First argument for adding method, defaults to 0
    :type number1: int | float, optional
    :param number2: Second argument for adding method, defaults to 0
    :type number2: int | float, optional
    :return: Sum of two arugments in the function
    :rtype: int | float

    >>> add(2, 3)
    5
    >>> add(2.3, 7.7)
    10.0
    """
    return number1 + number2


def sub(
    number1: int | float = 0,
    number2: int | float = 0,
) -> int | float:
    """Gets the difference between first number to the second number

    :param number1: First number from which the second number will
        be subtracted, defaults to 0
    :type number1: int | float, optional
    :param number2: Second number that to reduce the first number by,
        defaults to 0
    :type number2: int | float, optional
    :return: Subtraction of two numbers
    :rtype: int | float

    >>> sub(8, 2)
    6
    >>> sub(7.2, 3.1)
    4.1
    """
    return number1 - number2


def multiply(
    number1: int | float = 0,
    number2: int | float = 0,
) -> int | float:
    """Multiplying the first number with second number

    :param number1: First number to multiply from, defaults to 0
    :type number1: int | float, optional
    :param number2: Second number to be multiplied by, defaults to 0
    :type number2: int | float, optional
    :return: Multiplication of two numbers
    :rtype: int | float

    >>> multiply(4, 9)
    36
    >>> multiply(2.3, 8.2)
    18.86
    """
    return number1 * number2


def divide(
    divident: int | float = 1,
    divisor: int | float = 1,
) -> int | float:
    """Mathematical division of two numbers

    :param divident: The number which will be used to divident, defaults to 1
    :type divident: int | float, optional
    :param divisor: The number that will be the divsor, defaults to 1
    :type divisor: int | float, optional
    :raises ZeroDivisionError: If the number is divided by 0,
        it creates a mathematic error and therefore raises an error
    :return: divident / divisor
    :rtype: int | float
    """
    if divisor == 0:
        raise ZeroDivisionError('The divisor cannot be zero')
    return divident / divisor
