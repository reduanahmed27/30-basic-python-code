def convert_mint_to_hour(mint):
    div = int(mint/60)
    mod = mint%60
    return div , mod 
mint = float(input("Enter minutes: "))
hour,min = convert_mint_to_hour(mint)
print(f"{mint} is approxcimately {hour} hour and {min} minute")