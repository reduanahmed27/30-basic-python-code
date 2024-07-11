def valid_triangle(a1,a2,a3):
    r1 = a1**2
    r2 = (a2**2)+(a3**2)
    if r1==r2:
        return "Triangle is valid"
    else:
        return "Triangle isn't valid"

angle1 = int(input("Enter 1st angle: "))
angle2 = int(input("Enter 2nd angle: "))
angle3 = int(input("Enter 3rd angle: "))
print(valid_triangle(angle1,angle2,angle3))