__author__ = "730731576"


from find_max import find_and_remove_max


def test_return_value() -> None:
    assert find_and_remove_max(lst=[1, 8, 2, 3, 3]) == 8


def test_mutation() -> None:
    a: list[int] = [1, 8, 2, 3, 3]
    find_and_remove_max(a)
    assert a == [1, 2, 3, 3]


def test_unexpected_input() -> None:
    assert find_and_remove_max(lst=[]) == -1
