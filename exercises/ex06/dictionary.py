"""Dictionary Utility functions"""

__author__ = "730731576"


def invert(dct: dict[str, str]) -> dict[str, str]:
    """Inverts key : value pairs"""
    inverted_dct: dict[str, str] = {}
    for key in dct:
        val: str = dct[key]
        if val in inverted_dct:
            raise KeyError("Duplicate keys")
        inverted_dct[val] = key
    return inverted_dct


def favorite_color(dct: dict[str, str]) -> str:
    """Returns Color that appears most"""
    count: dict[str, int] = {}
    most: int = 0
    favorite: str = ""

    for key in dct:
        if dct[key] in count:  # checks if the color is already in the dict
            count[dct[key]] += 1
        else:  # adds the color if it isnt already in the dict
            count[dct[key]] = 1

    for key in count:
        if count[key] > most:
            most = count[key]
            favorite = key

    return favorite


def count(lst: list[str]) -> dict[str, int]:
    """Counts the number of occurrences in a list"""
    a: dict[str, int] = {}
    for x in lst:
        if x in a:
            a[x] += 1
        else:
            a[x] = 1
    return a


def alphabetizer(lst: list[str]) -> dict[str, list[str]]:
    """produce a dict where each key = a letter
    and each value = words starting with that letter"""
    a: dict[str, list[str]] = {}
    for x in lst:
        l: str = x[0].lower()
        if l in a:
            a[l].append(x)
        else:
            a[l] = [x]
    return a


def update_attendance(dct: dict[str, list[str]], day: str, student: str) -> None:
    """Appends students name to list in dict"""
    if day in dct and student not in dct[day]:
        dct[day].append(student)
    elif day not in dct:
        dct[day] = [student]
