"""
Testing to see if a number is a leap year
(leap years are divisible by 4 but not by 100 unless also divisible by 400)
"""

print("Enter a year, any year: ")

year = int(input('>'))

leap_year = False

if year % 4 == 0 and year % 100 != 0:
    leap_year = True
    print(f"It is {leap_year}, {year} is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    leap_year = True
    print(f"It is {leap_year}, {year} is a leap year")
else:
    print(f"{year} is not a leap year")
