"""Three functions that perform different actions on lists"""

__author__ = "730731576"


def only_evens(lst: list[int]) -> list[int]:
    """Returns a new list of only the even numbers"""
    evens: list[int] = []
    for x in lst:
        if x % 2 == 0:  # determines if even
            evens.append(x)
    return evens


def sub(lst: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Returns a section of a list"""
    if len(lst) == 0 or start_idx >= len(lst) or end_idx <= 0:
        return []
    # create a new list so the old one isnt mutated
    sub_lst: list[int] = []
    for i in range(0, len(lst)):
        if i >= start_idx and i < end_idx:
            sub_lst.append(lst[i])
    return sub_lst


def add_at_index(lst: list[int], val: int, idx: int) -> None:
    """Inserts a new value at a specific index"""
    if idx < 0 or idx > len(lst):
        raise IndexError("Index is out of bounds for the input list")

    lst.append(val)
    i: int = len(lst) - 1
    # starting at the end of the list prevents data from being overwritten
    while i > idx:
        lst[i] = lst[i - 1]
        lst[i - 1] = val
        i -= 1
