print("\tWelcome to 'Guess The Number'!")
print("\tThink of a number between 1 and 100.")
print("\tI will try to guess it in as few attempts as possible.\n")   

number = 50
higher = 101
lower = 0
guess = str(input("Is your number: {}".format(number)))
tries = 1
while guess not in ['Yes', 'yes', 'Y', 'y']:
    if guess in ['Higher', 'higher', 'H', 'h']:
        lower = number
        number = lower + (higher - lower) // 2
    if guess in ['L', 'Lower', 'l', 'lower']:
        higher = number
        number = higher - (higher - lower) // 2
    guess = str(input("Is your number: {}".format(number)))
    tries += 1
print("I guessed it! The number was", number)
print("And it only took me", tries, "tries!\n")
print("\n\nPress the enter key to exit.")