#Write a program to check whether the year is a leap year or not.

def find_leapyear(year):
    if (year%4==0 and year%100!=0):
        return True
    else:
        return False

try:
    year = int(input("Enter a year to find weather it is leap year or not: "))
    if year<=0:
        print("Please, enter a valid year")
    else:
        if find_leapyear(year):
            print(f"{year} is leap year")
        else:
            print(f"{year} is not leap year")
except ValueError:
    print("Enter a valid year")