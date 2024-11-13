def sum_of_evens(min_value, max_value):
    
    """
    Find the sum of even numbers between two given numbers (inclusive).

    Args:
        min_value (int): Minimum number
        max_value (int): Maximum number

    Returns:
        total: sum of the even numbers between min_value and max_value

    Example:

    min_value = 10
    max_value = 13
    total = sum_of_evens(min_value, max_value)
    print(total) # total is 22.
    """

    # Function implementation here ...
    
    if min_value < 1 or max_value < 1:
        print('invalid input, must be positive integers')
    
    elif min_value % 2 != 0:
        min_value += 1
    
    elif max_value % 2 != 0:
        max_value -= 1
    
    total = sum(range(min_value, max_value + 1, 2))
    
    return total


# Example result
result = sum_of_evens(1, 10)
print(result)