#Write a Program to enter P, T, and R and calculate simple interest.

def find_simple_interest(p,r,t):
    interest = (p*r*t)/100
    return interest

p = float(input("Enter principle amout$"))
r = float(input("Enter interest rate$"))
t = float(input("Enter time duration in year "))

simpleinterest = find_simple_interest(p,r,t)
print(f"simple interest = ${simpleinterest}")