__author__ = "730731576"


def find_and_remove_max(list: list[int]) -> int:
    if len(list) == 0:
        return -1
    max: int = list[0]
    for x in list:
        if x > max:
            max = x
    for i in range(0, len(list) - 1):
        if list[i] == max:
            list.pop(i)
    return max
