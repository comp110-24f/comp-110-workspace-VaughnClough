__author__ = "730731576"


def find_and_remove_max(lst: list[int]) -> int:
    if len(lst) == 0:
        return -1
    max_val: int = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x

    i = 0
    while i < len(lst) - 1:
        if lst[i] == max_val:
            lst.pop(i)
            i -= 1
        i += 1
    return max_val
