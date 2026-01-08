#guess a secret number between 1-10, keep asking until the guess is correct

correct_num = 6

attempt = 0

guess = int(input("Pick a number between 1 and 10: "))

while guess != correct_num:
    guess = int(input("Pick a number between 1 and 10: "))
    attempt += 1

    if guess == correct_num:
        print("Good job! You guessed it in {} attempts!" .format(attempt))
