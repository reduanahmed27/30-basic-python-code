def find_maximum(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
    
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print(f"Maximum number between {num1} & {num2} is {find_maximum(num1,num2)}")