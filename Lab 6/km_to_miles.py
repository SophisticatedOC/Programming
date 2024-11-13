# def km_to_miles(kilometers):
    # complete function implementation here...

def km_to_miles(km):
    if km < 0:
        print("Cannot enter a Negative value")
    miles = km * 0.62
    
    return round(miles, 3)

print(km_to_miles(120))