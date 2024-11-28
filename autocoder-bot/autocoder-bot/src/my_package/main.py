***
def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.

    Returns
    -------
    float
        The sum of the two numbers.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract one number from another.

    Parameters
    ----------
    a : float
        The number to be subtracted from.
    b : float
        The number to subtract.

    Returns
    -------
    float
        The result of the subtraction.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.

    Returns
    -------
    float
        The product of the two numbers.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide one number by another.

    Parameters
    ----------
    a : float
        The numerator.
    b : float
        The denominator.

    Returns
    -------
    float
        The result of the division.

    Raises
    ------
    ValueError
        If `b` is zero, a division by zero error will be raised.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
***
