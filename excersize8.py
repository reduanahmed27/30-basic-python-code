def fahrenit_to_celcius(fahrenhit):
    tempereture = (fahrenhit-32)/1.8
    return tempereture
fahrenhit = float(input("Enter tempereture in fahrenhit scale: "))
celcius = fahrenit_to_celcius(fahrenhit)
print(f"{fahrenhit} degree in fahrenhit is {celcius} degree in celcius.")