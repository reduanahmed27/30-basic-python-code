#Write a Program to calculate the area of an equilateral triangle.

import math
a = float(input("Enter size of an angle: "))
area = (math.sqrt(3)/4)*(a**2)
print(f"Area of equilateral triangle = {area:2F} m")