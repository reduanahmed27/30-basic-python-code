def tempereture_massage(temp):
    if temp>=-100 and temp<=100:
        if temp<0:
            return "Freezing weather"
        elif temp >=0 and temp<10:
            return "very cold weather"
        elif temp >=10 and temp<20:
            return "cold weather"
        elif temp>=20 and temp<30:
            return "Normal"
        elif temp>=30 and temp<40:
            return "It's hot"
        elif temp>=40:
            return "it’s very hot."
    else:
        return f"{temp} degree isn't recorded yet.Enter between -100 to 100 degree."
try:
    temp = int(input("Enter tempereture in centigrate: "))
    print(tempereture_massage(temp))
except ValueError:
    print("Enter a valid tempereture.")