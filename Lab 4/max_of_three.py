def max_of_three(num1, num2, num3):
    """
    This function takes three integers as input and returns the maximum of the three given numbers.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    num3 (int): The third number.

    Returns:
    int: The maximum of the three numbers.
    """
    # Hint: you are required to make use of maximum variable that is returned by the function below.
    # Complete your code implementation here...
    
    result1 = num1 > num2
    
    if result1 == True:
        result2 = num1 > num3
        if result2 == True:  
            maximum = num1
            print(f"The maximum is: {maximum}")
        elif result2 == False:
            maximum =num3
            print(f"The maximum is: {maximum}")
    
    elif result1 ==False:
        result2 = num2 > num3
        if result2 == True:
            maximum = num2
            print(f"The maximum is: {maximum}")
        elif result2 == False:
            maximum = num3
            print(f"The maximum is: {maximum}")
    
    return maximum

# # You are out of the body function where you can test your code.
# Example usage:
# maximum = max_of_three(10, 20, 30)
# print(maximum, "is the maximum")
max_of_three(40, 30, 30)