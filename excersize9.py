#Write a Program to enter marks of five subjects and calculate the total, 
#average, and percentage.

print("Enter marks in five subjects: ")
subjects=[]
total = 0

for i in range(5):
    sub = int(input(f"Subject{i+1} = "))
    subjects.append(sub)
    total = total+sub
    average = total/5
    percentage = (total/500)*100

print(f"Total marks = {total} out of 500")
print(f"Average marks = {average}")
print(f"percentage in each subjects = {percentage}%")