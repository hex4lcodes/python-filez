import math

#defining and storing vars for og number and choice

print("Enter a number in either radians or degrees: ")

number = float(input(">"))

print("Pick a choice, R for radians, D for dgrees: ")

choice = input(">")


#the if-statement to test conditions

if choice == 'r' or choice == 'R':
    print(math.radians(number))
elif choice == 'd' or choice == 'D':
    print(math.degrees(number))
else:
    print("Incorrect choice! Start over!")
