"""ex04 - list utils"""

__author__ = "730731576"


def all(list: list[int], val: int) -> bool:
    for x in list:
        if x != val:
            return False
    return True


def max(list: list[int]) -> int:
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    max: int = 0
    for x in list:
        if x > max:
            max = x
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    for x in range(
        0, len(list1)
    ):  # used range so x can be used for indexing both lists
        if list1[x] != list2[x]:
            return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    for x in list2:
        list1.append(x)
