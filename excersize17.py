#Write a program to find the maximum between three numbers.

def find_maximum(num1,num2,num3):
    if num1>num2:
        return num1
    elif num1>num3:
        return num1
    elif num2>num3:
        return num2
    else:
        return num3
    
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

print(f"Maximum number is {find_maximum(num1,num2,num3)}")