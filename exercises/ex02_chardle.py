"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730731576"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        return word


# I can use letter and word as variables in the above and below functions
# as well as in contains_char() because they are not in the same scope


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()
        return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for", letter, "in", word)
    count: int = 0
    # It is weird to do this without a loop
    if word[0] == letter:
        print(letter, "found at index 0")
        count += 1
    if word[1] == letter:
        print(letter, "found at index 1")
        count += 1
    if word[2] == letter:
        print(letter, "found at index 2")
        count += 1
    if word[3] == letter:
        print(letter, "found at index 3")
        count += 1
    if word[4] == letter:
        print(letter, "found at index 4")
        count += 1
    if count == 0:
        print("No instances of", letter, "found in", word)
    elif count == 1:
        print("1 instance of", letter, "found in", word)
    else:
        print(count, "instances of", letter, "found in", word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
