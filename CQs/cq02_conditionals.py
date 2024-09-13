"""Challenge question 02"""

__author__ = "730761576"


def guess_a_number() -> None:
    secret: int = 7
    guess = int(input("Guess a number: "))
    print("Your guess was", guess)
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is", secret)
    else:
        print("Your guess was too high! The secret number is", secret)


if __name__ == "__main__":
    guess_a_number()
