"""ex03 - Wordle"""

__author__ = "730731576"


def input_guess(secret_len: int) -> str:
    while True:  # Starts an infinite loop
        guess = input(f"Enter a {secret_len} character word: ")
        if len(guess) != secret_len:
            print(f"That wasn't {secret_len} chars! Try again:")
        else:
            return guess


def contains_char(word: str, char: str) -> bool:
    """Checks to see if the word contains a character"""
    assert len(char) == 1
    i = 0
    while i < len(word):
        if char == word[i]:
            return True
        i += 1
    return False


def emojified(guess: str, word: str) -> str:
    """Checks accuracy of guess and converts to emojies"""
    assert len(guess) == len(word)
    emojies = ""
    i = 0
    while i < len(word):
        if word[i] == guess[i]:
            emojies += "\U0001F7E9"
        elif contains_char(
            word, guess[i]
        ):  # "if contains_char" is a valid because the function's returns a bool
            emojies += "\U0001F7E8"
        else:
            emojies += "\U00002B1C"
        i += 1
    return emojies


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1
    while turn <= 7:
        if turn == 7:
            print("X/6 - Sorry, try again tomorrow!")
            exit()  # exit so that it doesnt go on to print the next statement
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            exit()  # exit so it doesnt continue the loop
        turn += 1


if __name__ == "__main__":
    main(secret="codes")
