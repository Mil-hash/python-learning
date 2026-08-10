secret = 7
guess = 0
tries = 0

while guess != secret:
    guess = int(input("Guess the number: "))
    tries = tries + 1

    if guess == secret:
        print("Correct! You got it in " + str(tries) + " tries.")

    elif guess > secret:
        print("too high")

    else: 
        print("too low")
