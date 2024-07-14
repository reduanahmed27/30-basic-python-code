#Write a program to find the power of any number x ^ y

def find_power(num,pow):
    r = num**pow
    return r

num = int(input("Enter any number: "))
pow = int(input("Enter power: "))
result = find_power(num,pow)
print(f"The value of {num}^{pow} is = {result}")