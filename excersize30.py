def last_digit(number):
    return number % 10

try:
    num = int(input("Enter an integer: "))
    last_digit = last_digit(num)
    print(f"The last digit of {num} is: {last_digit}")
except ValueError:
    print("Invalid input. Please enter an integer.")