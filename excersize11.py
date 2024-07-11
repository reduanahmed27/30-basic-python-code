def find_advance_interest(p,r,t):
    interest = p*(1+(r/100))**t
    return interest

p = float(input("Enter principle amout $"))
r = float(input("Enter interest rate $"))
t = float(input("Enter time duration in year "))

advanceinterest = find_advance_interest(p,r,t)
print(f"Advance interest = ${advanceinterest}")