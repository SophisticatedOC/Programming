# def annual_net_income(gross_salary):
    # complete your function implementation here...

def annual_net_income(gross_salary):
    if gross_salary >= 45000:
        tax_rate = 0.50
    elif 30000 <= gross_salary < 45000:
        tax_rate = 0.30
    else:
        tax_rate = 0.15
    net_income = gross_salary * (1 - tax_rate)
    return net_income

print(annual_net_income(60000))
print(annual_net_income(30000))
print(annual_net_income(20000))