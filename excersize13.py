def convert_days_into_year(days):
    year = int(days/365)
    mod = int(days%365)
    week = int(mod/7)
    day = int(week/7)
    return year,week,day

days = float(input("Enter days: "))
year,week,day = convert_days_into_year(days)
print(f"{days} is approxcimately {year} year, {week} week, {day} days.")