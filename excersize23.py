def vowel_consonent(char):
    vowel = "aeiou"
    lowerchar = char.lower()

    if lowerchar in vowel:
        return "The character is vowel"
    else:
        return "The character is consonent"
try:
    char = input("Enter any character from a-z: ")
    if len(char)!=1:
        print("Please enter a sinle character.")
    else:
        print(vowel_consonent(char))
except ValueError:
    print("Please enter a valid character.")