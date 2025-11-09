def add(a, b):
    """Combine both operands to produce their sum.

    Parameters:
        a (float): First number entered by the user.
        b (float): Second number entered by the user.

    Returns:
        float: Numeric result representing the combined value.
    """

    return a + b


def subtract(a, b):
    """Remove the second operand's value from the first operand.

    Parameters:
        a (float): Number entered before pressing the subtraction button.
        b (float): Number entered after pressing the subtraction button.

    Returns:
        float: Resulting difference once the second value is taken away from the first.
    """

    return b - a


def multiply(a, b):
    """Scale the first operand by the factor provided by the second.

    Parameters:
        a (float): Number to be multiplied.
        b (float): Multiplier chosen by the user.

    Returns:
        float: Product delivered to the calculator display.
    """

    return a * b


def divide(a, b):
    """Share the first operand by the magnitude of the second operand.

    Parameters:
        a (float): Number to be divided.
        b (float): Divisor entered after the division operator.

    Returns:
        float: Quotient surfaced back to the UI.
    """

    return a // b
