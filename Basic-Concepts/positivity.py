#ask user to enter positive numbers
#stop when users enter negative numbers - while loop

num_guess = int(input("Enter a positive number: "))

while num_guess >= 0:
    num_guess = int(input("Enter a positive number: "))

    if num_guess < 0:
        break
    else:
        pass
