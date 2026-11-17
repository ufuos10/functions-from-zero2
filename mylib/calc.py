"""
A Calculator module that provides basic arithmetic operations.
"""


def add(a, b):
    """
    Add two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b


def subtract(a, b):
    """
    Subtract two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference of a and b.
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b.
    """
    return a * b


def divide(a, b):
    """
    Divide two numbers.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The quotient of a and b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# build a function to calculate the power of a number with x as the base and y as the exponent
def power(x, y):
    """
    Calculate the power of a number.

    Args:
        x (float): The base number.
        y (float): The exponent.

    Returns:
        float: The result of x raised to the power of y.
    """
    return x**y


# build a function to calculate the square root of a number
def square_root(x):
    """
    Calculate the square root of a number.

    Args:
        x (float): The number to calculate the square root of.

    Returns:
        float: The square root of x.

    Raises:
        ValueError: If x is negative.
    """
    if x < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return x**0.5
