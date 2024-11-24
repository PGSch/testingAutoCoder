{
  "functions": [
    {
      "name": "add",
      "code": "def add(a: float, b: float) -> float:
    \"\"\"
    Add two numbers.

    Parameters
    ----------
    a : float
        The first number to add.
    b : float
        The second number to add.

    Returns
    -------
    float
        The sum of a and b.
    \"\"\"
    return a + b"
    },
    {
      "name": "subtract",
      "code": "def subtract(a: float, b: float) -> float:
    \"\"\"
    Subtract two numbers.

    Parameters
    ----------
    a : float
        The number from which to subtract.
    b : float
        The number to be subtracted.

    Returns
    -------
    float
        The result of a - b.
    \"\"\"
    return a - b"
    },
    {
      "name": "multiply",
      "code": "def multiply(a: float, b: float) -> float:
    \"\"\"
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
        The product of a and b.
    \"\"\"
    return a * b"
    },
    {
      "name": "divide",
      "code": "def divide(a: float, b: float) -> float:
    \"\"\"
    Divide one number by another.

    Parameters
    ----------
    a : float
        The numerator.
    b : float
        The denominator.

    Raises
    ------
    ValueError
        If b is zero, a division by zero error occurs.

    Returns
    -------
    float
        The result of a divided by b.
    \"\"\"
    if b == 0:
        raise ValueError('Denominator cannot be zero.')
    return a / b"
    }
  ]
}
