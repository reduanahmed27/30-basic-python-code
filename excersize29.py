#Write a program to find the sum of all even numbers between 1 to n.

def sum_of_even(n):
    sum = 0
    i = 2
    for i in range(2, n+1, 2):
        sum = sum + i
        i = i+2
    return sum
try:
    n = int(input("Enter value of n: "))
    print(sum_of_even(n))
except ValueError:
    print("Enter valid number")