"""Test my zip function."""
__author__ = "730664658"

from lessons.zip import zip


def test_empty_list() -> None:
    """Testing that empty lists should return an empty dictionary."""
    word_list: list[str] = []
    num_list: list[int] = []
    dict1 = {}
    assert zip(word_list, num_list) == dict1


def test_lists_with_length_1() -> None:
    """Testing lists with 1 element."""
    word_list: list[str] = ["Hello"]
    num_list: list[int] = [1]
    dict1 = {"Hello": 1}
    assert zip(word_list, num_list) == dict1


def test_lists_unequal_amount_of_elements() -> None:
    """Testing if len(word_list) != len(num_list)."""
    word_list: list[str] = ["Hello"]
    num_list: list[int] = [1, 2, 3]
    dict1 = {}
    assert zip(word_list, num_list) == dict1