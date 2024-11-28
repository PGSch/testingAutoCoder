def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float
        The first number to multiply.
    b : float
        The second number to multiply.

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
    ZeroDivisionError
        If `b` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b
