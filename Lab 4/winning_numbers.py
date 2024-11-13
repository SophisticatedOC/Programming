def winning_numbers(unum1, unum2, unum3):
    """
    This function checks if the user's numbers match the predefined winning numbers.

    Parameters:
    user_numbers (list): A list of three integers representing the user's chosen numbers.
    winning_numbers (list): A list of integers representing the winning numbers.

    Returns:
    str: A string indicating the prize won:
        - "First" if all three numbers match the winning numbers.
        - "Second" if two numbers match the winning numbers.
        - "Third" if one number matches the winning numbers.
        - "No" if none of the numbers match the winning numbers.

    Example:
    --------
    winning_numbers = [5, 14, 17]
    user_numbers = [3, 5, 10]
    result = winning_numbers(user_numbers, winning_numbers)
    # Output: "Third" (since one number, 5, matches the winning numbers)

    user_numbers = [14, 5, 10]
    result = winning_numbers(user_numbers, winning_numbers)
    # Output: "Third" (since two numbers, 14 and 5, match the winning numbers)

    The function also prints a message indicating the prize won.
    """

    # Function implementation here ...
    
    wnum1 = 5
    wnum2 = 10
    wnum3 = 14
    
    win = 0
    
    if unum1 == wnum1:
        win += 1
    else:
        win + 0 
    
    if unum2 == wnum2:
        win += 1
    else:
        win + 0
        
    if unum3 == wnum3:
        win += 1
    else:
        win + 0
        
    if win == 3:
        prize = "first"
    elif win == 2:
        prize = "second"
    elif win == 1:
        prize = "third"
    else:
        prize = "No"
    
    # Print the result
    print(f"Congratulations, you won {prize} prize!")

    return prize

# Test
winning_numbers(5, 10, 14)
winning_numbers(5, 10, 12)
winning_numbers(5, 8, 12)
winning_numbers(3, 8, 12)
