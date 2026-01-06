"""
Password checker

Thank you to Reddit user LebronJayce for what became the shell for this project!!
And thanks to the wonderful folks at GeeksforGeeks for the explanations!!

Password must have: 8 characters, both upper and lowercase letters, at least one number
"""

print("Enter a password below (plese ommitt special charaters!): ")

password = input('> ')

if len(password) < 8:
    print("Password too short, try again!")
    exit()
else:
    pass

if password.isalnum() and not password.isdigit() and not password.isalpha(): #will test to see if password is alphanumeric - not just letter / number only
    pass
else:
    pass

n = any(password.isdigit() for char in password) #will check to see if any character in password is uppercase

if n:
    print("Strong password!")
    exit()
else:
    print("Password not strong! Must contain an uppercase letter")

if password.isdigit():
    print("Password cannot contain only numbers, password must contain letters and numbers")
    exit()
else:
    pass

if password.isalpha():
    print("Password cannot contain only letters, password must contain letters and numbers")
    exit()
else:
    pass
