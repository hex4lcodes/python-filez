#this came from the exact book Im using for the C projects (which actual code projects are coming soon )
#i just decided to make it in Python


#gathering begining and ending mileage

print("Enter starting mileage: ")
begmile = int(input('>'))

print("Enter ending mileage: ")
endmile = int(input('>'))


#calculations

travel = endmile - begmile
rate = 0.575

reimburse = travel * rate

print("You traveled {} miles. At a rate of {} per mile, your reimbursement is: {:.4}" .format(travel, rate, reimburse))
#im going to round the numbers to 4 decimals
