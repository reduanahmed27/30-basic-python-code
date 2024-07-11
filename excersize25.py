a = """
the eligibility for admission to a professional
course base on the following criteria:
Marks in MATHS >= 65
Marks in PHY >= 55
Marks in CHEM >= 50
Or,
Total in all three subjects => 180
Or,
Total in Math and physics >=140.
"""
print(a)
def eligibility (s1,s2,s3):
    if s1>=65 and s2>=55 and s3>=50 or total>=180 or s1+s2>=140:
        return "eligibility for admission"
    else:
        return "Not eligibility for admission"

s1 = int(input("Enter marks is math: "))
s2= int(input("Enter marks is Physics: "))
s3 = int(input("Enter marks is CHemistry: "))
total = s1+s2+s3
print(eligibility(s2,s2,s3))