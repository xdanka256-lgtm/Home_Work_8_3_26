
def input_until_lucky(lucky_numbers: tuple) -> int:
    attempts = 0
    while True:
        try:
            guess = int(input("Guess a lucky number"))
            attempts += 1
            if guess in lucky_numbers:
                return attempts
            attempts += 1
        except ValueError:
            print("Invalid input, please enter a number")
