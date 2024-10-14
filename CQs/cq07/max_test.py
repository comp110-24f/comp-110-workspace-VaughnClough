__author__ = "730731576"


from find_max import find_and_remove_max


def test_return_value() -> None:
    assert find_and_remove_max(list=[1, 3, 6, 2]) == 6


def test_mutation() -> None:
    a: list[int] = [1, 3, 6, 2]
    find_and_remove_max(a)
    assert a == [1, 3, 2]


def test_unexpected_input() -> None:
    assert find_and_remove_max(list=[]) == -1
