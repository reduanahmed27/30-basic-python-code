def find_oddeven(num):
    if num%2==0 :
        return "Number is Even"
    else :
        return "Number is odd"
num = int(input("Enter any number: "))
print(find_oddeven(num))