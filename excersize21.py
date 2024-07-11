def citizenship (s1,s2,s3):
    if s1==s2 and s2==s3:
        return ("You are eligible to make NID card.")
    else:
        return ("You aren't eligible to make NID card.")

s1 = input("Are you citizen of Bangladesh ? Enter (y/n): ")
s2 = input("Are you 18 years old ? Enter (y/n): ")
s3 = input("Did you registered before ? Enter (y/n): ")
print(citizenship(s1,s2,s3))