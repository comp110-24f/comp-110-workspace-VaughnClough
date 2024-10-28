"""Tests utils.py"""

__author__ = "730731576"


from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_return() -> None:
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_only_evens_mutation() -> None:
    a: list[int] = [1, 2, 3, 4]
    only_evens(a)
    assert a == [1, 2, 3, 4]


def test_only_evens_edge() -> None:
    assert only_evens([]) == []


def test_sub_return() -> None:
    assert sub([1, 2, 3, 4], 1, 2) == [2, 3]


def test_sub_mutation() -> None:
    a: list[int] = [1, 2, 3, 4]
    sub(a, 1, 3)
    assert a == [1, 2, 3, 4]


def test_sub_edge() -> None:
    assert sub([], 1, 3) == []


def test_insert_return() -> None:
    assert add_at_index([1, 2], 3, 2) == None


def test_insert_mutation() -> None:
    a = [1, 3, 4]
    add_at_index(a, 2, 1)
    assert a == [1, 2, 3, 4]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    with pytest.raises(IndexError):
        add_at_index([1, 2, 3], 1, 5)
