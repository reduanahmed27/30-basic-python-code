#Write a program to enter any number and calculate its square root.

import math
def find_sqrtroot(num):
    r = math.sqrt(num)
    return r
num = int(input("Enter any number: "))
result = find_sqrtroot(num)
print(f"sqrtroot of {num} is {result}")