def calculate_weekly_pay(hours_worked):
    """
    Calculate the weekly pay for an employee based on the number of hours worked.
    
    Parameters:
    hours_worked (int): The total number of hours worked by the employee in a week.
    
    Returns:
    float: The total weekly pay.
    """

    # Function implementation here ...

    if hours_worked < 0:
        raise ValueError("Total hours must be a positive value.")
    
    regular_rate = 12
    overtime_rate = 18

    if hours_worked <= 35:
        total_pay = hours_worked * regular_rate
        
    else:
        regular_pay = 35 * regular_rate
        overtime_hours = hours_worked - 35
        overtime_pay = overtime_hours * overtime_rate
        total_pay = regular_pay + overtime_pay

    return total_pay
    
print(calculate_weekly_pay(38))
