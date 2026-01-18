
import datetime

#getting the date
print("Enter the year of the random date in the format yyyy: ")
yeaur = int(input('>'))

print("Enter the year of the random date in the format mm: ")
month = int(input('>'))

print("Enter the year of the random date in the format dd: ")
day = int(input('>'))

#formatting the date
randomdate = datetime.datetime(yeaur, month, day)



# get day of week as an integer
x = randomdate.weekday()

#print the actual day of the week
if x == 0:
    print(f"{randomdate}, Monday")
elif x == 1:
    print(f"{randomdate}, Tuesday")
elif x == 2:
    print(f"{randomdate}, Wednesday")
elif x == 3:
    print(f"{randomdate}, Thursday")
elif x == 4:
    print(f"{randomdate}, Friday")
elif x == 5:
    print(f"{randomdate}, Saturday")
elif x == 6:
    print(f"{randomdate}, Sunday")
else:
    pass
