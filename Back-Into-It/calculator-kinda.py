#this is gonna be a pretty basic calculator (big 4 operations (+,-,*,/) and radians and degrees)
#the values are stored as floats to account for values used in radians and degree calculations

#exit stops the program if a block evaluates to true

#fixed the or statement to more accurately compute each block

import math

print("This calcualtor allows for additon, subraction, multiplication, division, radians and degrees")
print("If you have only one number to work with fill in 0 for the second value")

print("\n")

print("Enter the first number you will be working with")
val1 = float(input(">"))

print("Enter the second number you will be working with")
val2 = float(input(">"))

print("\n")

print("What calculation would you like to do: a addition, s subtraction, m multiplication, g for division")
print("You can use D for degrees and R for radians")
operation = input(">")

if operation == 'a' or operation == 'A':
    print(val1 + val2)
    exit()
elif operation == 's' or operation == 'S':
    print(val1 - val2)
    exit()
elif operation == 'm' or operation == 'M':
    print(val1 * val2)
    exit()
elif operation == 'g' or operation == 'G' and val2 != 0: 
    if val2 == 0 and operation == 'g' or operation == 'G':
        print("Anything divided by 0 is 0, use your brain!")
        exit()
    else:
        pass
    print(val1/val2)
    exit()
else:
    pass





if operation == 'd' or operation == 'D':
    print(math.degrees(val1))
    pass
    if  val2 != 0:
        print(math.degrees(val2))
        exit()
    else:
        pass
elif operation == 'r' or operation == 'R':
    print(math.radians(val1))
    pass

    if  val2 != 0:
        print(math.radians(val2))
        exit()
    else:
        pass
else:
    print("Something went wrong, try again")

