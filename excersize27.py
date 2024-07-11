def evaluate_expression(a, b, c, d):
    if c - d != 0:
        result = (a + b) / (c - d)
        print(f"The result of ({a} + {b}) / ({c} - {d}) is: {result:.2f}")
    else:
        print("Error: Division by zero (c - d is zero).")

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = float(input("Enter the value of d: "))