def add(a, b):
    """
    Add two numbers together.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.

    Returns
    -------
    float
        The sum of `a` and `b`.
    """
    return a + b


def subtract(a, b):
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
        The result of `a` minus `b`.
    """
    return a - b


def multiply(a, b):
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
        The product of `a` and `b`.
    """
    return a * b


def divide(a, b):
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
        The result of `a` divided by `b`.

    Raises
    ------
    ValueError
        If `b` is zero, an error is raised because division by zero is undefined.
    """
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b
