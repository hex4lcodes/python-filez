#changing users birthday format to dd/mm/yyy

import datetime

#getting the birthdate
print("Enter the year you were born in the format mm: ")
birth_year = int(input('>'))

print("Enter the month you were born in the format mm: ")
birth_month = int(input('>'))

print("Enter the date you were born in the format dd: ")
birth_day = int(input('>'))

date = datetime.datetime(birth_year, birth_month, birth_day)
dob = date.strftime("%d/%m/%Y")

print(date)

print(f"Formatted date of birth: {dob}")
