"""cq03 While loops"""

__author__ = "730731576"


def num_instances(phrase: str, search_char: str) -> int:
    i = 0
    count = 0
    while i < len(phrase):
        if phrase[i] == search_char:  # use i as the iterator and to go through phrase
            count += 1  # adds 1 to count
        i += 1
    return count