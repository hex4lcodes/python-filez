#how many days until users next birthday

import datetime

#getting the birth month and day
print("Enter the month you were born in the format mm: ")
birth_month = int(input('>'))

print("Enter the date you were born in the format dd: ")
birth_day = int(input('>'))

#formatting the birthday
year = 2026
date = datetime.datetime(year, birth_month, birth_day)

today = datetime.datetime.now() #the date and time the program is ran at

days_left = date - today

print("There are {} days left until your birthday!" .format(days_left.days)) #takes only the days
