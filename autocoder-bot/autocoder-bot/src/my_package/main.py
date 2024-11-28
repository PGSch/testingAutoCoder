
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
        The denominator. Must not be zero.

    Returns
    -------
    float
        The result of the division.

    Raises
    ------
    ValueError
        If b is zero, raises an error to indicate division by zero.
    """
    if b == 0:
        raise ValueError("Denominator b must not be zero.")
    return a / b
