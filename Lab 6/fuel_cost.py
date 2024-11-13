# def fuel_cost(distance_miles):
#     # Constants
#     MPG = 50  # Miles per gallon
#     LITERS_PER_GALLON = 4.5
#     PRICE_PER_LITER = 1.49  # Price in pounds per liter
#     continue function implementation here...

def fuel_cost(distance_miles):
    MPG = 50
    LPG = 4.5
    PPL = 1.49
    
    gallons_needed = distance_miles / MPG
    liters_needed = gallons_needed * LPG
    total_cost = liters_needed * PPL
    
    return total_cost

print(fuel_cost(50))