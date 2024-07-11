def divisible(num):

    if num>=5:
        if num%5==0:
            return "Number is divisible by 5" 
        elif num%11==0:
            return "Number is divisible by 11"
        else:
            return "number isn't divisible by 5 or 11"
    else:
            return "number isn't divisible by 5 or 11"
num = int(input("Enter any number: "))
print(divisible(num))