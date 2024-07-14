#Write a program to check whether a number is negative, positive, or zero

def find_pos_neg(num):
    if num>0:
        return "number is positive"
    elif num<0:
        return "number is negative"
    else:
        return "number is zero"
    
num = int(input("Enter any number: "))
print(find_pos_neg(num))