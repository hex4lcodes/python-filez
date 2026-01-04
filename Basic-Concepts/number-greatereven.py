#for the number, greater than 10 must be true AND even must be true
#if not print an error method

print("Enter any number: ")
n = int(input('>'))

if n > 10 and n % 2 == 0: #n % 2 == 0 tests to see if a number divides by 2 with no remainder
    print("The number {} works. Thanks!" .format(n))
else:
    print("Invalid Input")
