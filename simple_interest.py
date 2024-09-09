# simple_interest.py

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest using the formula:
    SI = (P * R * T) / 100
    where:
    P = principal amount
    R = rate of interest
    T = time period in years
    """
    return (principal * rate * time) / 100

if _name_ == "_main_":
    # Sample inputs
    principal = 1000
    rate = 5
    time = 2

    interest = calculate_simple_interest(principal, rate, time)
    print(f"Simple Interest: {interest}")
