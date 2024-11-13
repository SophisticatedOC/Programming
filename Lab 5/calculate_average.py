def calculate_average(numbers):
    """
    This function calculates the average of a list of numbers using a for loop.

    Parameters:
    ----------
    numbers : list
        A list of numerical values (int or float).

    Returns:
    -------
    float:
        The average of the numbers in the list. If the list is empty, returns None.

    Example:
    --------
    calculate_average([10, 20, 30, 40, 50])  # Output: 30.0
    """

    # Function implementation here ...

    if not numbers:
        return 0
    
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    
    return average

print(calculate_average([1, 2, 3, 4, 5]))