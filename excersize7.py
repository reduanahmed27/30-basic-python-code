def celcius_to_fahrenhit(celcius):
    tempereture = (9/5)*celcius+32
    return tempereture
celcius = float(input("Enter tempereture in celcius scale: "))
fahrenhit = celcius_to_fahrenhit(celcius)
print(f"{celcius} digree in celcius is {fahrenhit} degree in fahrenhit.")