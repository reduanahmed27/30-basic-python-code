#Write a program to enter the length, and breadth of a rectangle and find its 
#perimeter and area.

length = float(input("Enrter length:"))
breadth = float(input("Enter breadth:"))
area = length*breadth
perimiter = 2*(length*breadth)
print(f"Area of rectangle = {area}m")
print(f"perimiter of rectangle = {perimiter}m")