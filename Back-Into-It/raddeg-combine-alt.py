import math

#defining and storing vars for og number and choice

print("Enter a number in either radians or degrees: ")

number = float(input(">"))

print("Pick a choice, R for radians, D for dgrees: ")

choice = input(">")


#the if-statement to test conditions

if choice == 'r' or choice == 'R':
    if number <= 6.28319: #2pi is approx that number
        print(math.radians(number))
    else:
        print("Invalid input, try again")
elif choice == 'd' or choice == 'D':
    if number <= 360: #360 degrees is a full circle
        print(math.degrees(number))
    else:
        print("Invalid input, try again")
else:
    print("Incorrect choice! Start over!")
