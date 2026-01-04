import math

#defining and storing vars for og number and choice

print("Enter a number in either radians or degrees: ")

number = float(input(">"))

print("Pick a choice, R for radians, D for dgrees: ")

choice = input(">")


#the if-statement to test conditions

if choice == 'r' or choice == 'R':
    if number <= 6.28319:
        print(math.radians(number))
    else:
        print("Invalid input, try again")
elif choice == 'd' or choice == 'D':
    if number <= 360:
        print(math.degrees(number))
    else:
        print("Invalid input, try again")
else:
    print("Incorrect choice! Start over!")
