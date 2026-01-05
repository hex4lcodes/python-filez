"""
A real multi-line comment !! lololol

conditions: (1) both numbers must be greater than 100 for the first if statement
            (2) either number must be greater than 100 for the second
"""

#asking if user wants to play
print("Would you like to play? ")

playing = input('>')

if playing == 'yes' or playing == "YES" or playing == 'Yes':
    pass
else:
    exit()

print("Yayyy! thanks for deciding to playyy!!")

#gathering the numbers

print("Pick your first number: ")

firstnum = int(input('>'))

print("Now pick the second: ")

secondnum = int(input('>'))

#testing

if firstnum > 100 and secondnum > 100:
    print("Good choice, +5 points for you!")
    pass
else:
    print("Not this round, lets try again next round..")


if firstnum > 100 or secondnum > 100:
    print("Good choice, +5 points for you!")
    pass
else:
    print("No points for you this round...")



#maybe we can extend this and do something with the point system
