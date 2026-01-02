
#idea - allow any number but have an if statement to check to see if its between 0-22

#.. then if it is return factorial, if not return invalid error

import math 

print("Enter a number: ")

num = int(input(">"))

if num <= 22:
    print(math.factorial(num))

else:
    print("Error: number too high")


#its --> import math NOT #import math
