def add(a: float, b: float) -> float:
    """
    Add two numbers together.

    Parameters
    ----------
    a : float
        The first number to add.
    b : float
        The second number to add.

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
        The number to subtract from.
    b : float
        The number to be subtracted.

    Returns
    -------
    float
        The result of the subtraction.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers together.

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
    ValueError
        If the denominator is zero.
    """
    if b == 0:
        raise ValueError('Denominator cannot be zero.')
    return a / b
