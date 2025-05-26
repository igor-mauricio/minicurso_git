import math
def log_natural(x):
    """
    Calculate the natural logarithm of a number.

    Parameters:
    x (float): The number to calculate the natural logarithm for.

    Returns:
    float: The natural logarithm of x.
    
    Raises:
    ValueError: If x is less than or equal to zero.
    """
    if x <= 0:
        raise ValueError("Input must be greater than zero.")
    
    return math.log(x)