def check_number(num):
    """
    Check if the given number is less than 2 and print an alert if it is.

    Parameters:
    num (int or float): The number to be checked.

    Returns:
    str: Alert message if the number is less than 2, otherwise a confirmation message.
    
    Example:
    >>> check_number(1.5)
    'Alert: The number is less than 2!'
    >>> check_number(3)
    'The number is 2 or greater.'
    """
    if num < 2:
        return "Alert: The number is less than 2!"
    else:
        return "The number is 2 or greater."

# Example usage:
print(check_number(1.5))
print(check_number(3))
