"""Testing our dictionary functions."""

__author__ = "730664658"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_empty_dict_for_invert() -> None:
    """Testing that an empty dictionary for invert function should just return an empty dictionary."""
    dictionary: dict[str, str] = {}
    inverted: dict[str, str] = {}

    assert invert(dictionary) == inverted


def test_short_dict_for_invert() -> None:
    """Testing a short dictionary for invert function and it will return inverted dictionary."""
    dict1: dict[str, str] = {"a": "z", "b": "y"}
    inverted: dict[str, str] = {'z': 'a', 'y': 'b'}

    assert invert(dict1) == inverted


def test_complex_dict_for_invert() -> None:
    """Testing a longer dictionary and longer strings for invert function and it will return inverted dictionary."""
    dict1: dict[str, str] = {"a": "z", "b": "y", "apples": "bananas", "jonathan": "hu", "red": "blue"}
    inverted: dict[str, str] = {'z': 'a', 'y': 'b', 'bananas': 'apples', 'hu': 'jonathan', 'blue': 'red'}

    assert invert(dict1) == inverted


def test_raise_key_error_for_invert() -> None:
    """Testing that it raises a KeyError when encountering more than one of the same key."""
    with pytest.raises(KeyError):
        my_dictionary = {'john': 'doe', 'tim': 'doe'}
        invert(my_dictionary)


def test_if_dictionary_empty_for_favorite_color() -> None:
    """If the input dictionary is empty, function should return empty string."""
    col: dict[str, str] = {}
    popular_color: str = ""

    assert favorite_color(col) == popular_color


def test_favorite_color_default() -> None:
    """Testing a normal use of function, with one color being the most popular, should return that color."""
    col: dict[str, str] = {"j": "blue", "k": "blue", "m": "red", "o": "yellow"}
    popular_color: str = "blue"

    assert favorite_color(col) == popular_color


def test_favorite_color_two_most_popular_colors() -> None:
    """Testing that if two colors are equally the most popular, the favorite color will be the first one to be counted as popular."""
    col: dict[str, str] = {"j": "blue", "k": "blue", "m": "red", "o": "red"}
    popular_color: str = "blue"

    assert favorite_color(col) == popular_color


def test_count_for_0_times() -> None:
    """Testing that if the list is empty then the dicionary should be empty."""
    a: list[str] = []
    dict1: dict[str, int] = {}

    assert count(a) == dict1


def test_count_for_normal_list() -> None:
    """Testing a normal list of strings, should return a dictionary with keys and their values (count)."""
    a: list[str] = ["nc", "nc", "nc", "sc", "ga", "ny"]
    dict1: dict[str, int] = {'nc': 3, 'sc': 1, 'ga': 1, 'ny': 1}

    assert count(a) == dict1


def test_count_for_normal_list_but_out_of_order() -> None:
    """Testing a normal list of strings, but with a string appearing not necessarily after the same string."""
    a: list[str] = ["ny", "sc", "nc", "nc", "ga", "nc"]
    dict1: dict[str, int] = {'nc': 3, 'sc': 1, 'ga': 1, 'ny': 1}

    assert count(a) == dict1


def test_empty_list_for_alphabetizer() -> None:
    """Testing that an empty list would result in function returning empty dictionary."""
    a: list[str] = []
    dict1: dict[str, list[str]] = {}

    assert alphabetizer(a) == dict1


def test_one_unique_letter_for_alphabetizer() -> None:
    """Testing a list with a one unique first letter, that should just return a dictionary with the first letter as key and value as list of those words with that first letter."""
    a: list[str] = ["Bobby", "ball", "brick"]
    dict1: dict[str, list[str]] = {'b': ['Bobby', 'ball', 'brick']}

    assert alphabetizer(a) == dict1


def test_multiple_unique_letter_for_alphabetizer() -> None:
    """Testing a list with multiple unique first letter, should return a dictionary with unique letter corresponding with list of words with that first unique letter."""
    a: list[str] = ["Bobby", "ball", "brick", "april", "cheese", "Apple", "Can", "brown"]
    dict1: dict[str, list[str]] = {'b': ['Bobby', 'ball', 'brick', 'brown'], 'a': ['april', "Apple"], 'c': ['cheese', 'Can']}

    assert alphabetizer(a) == dict1


def test_entering_no_same_name_for_day() -> None:
    """Testing that the same name is not repeated for the same day and cannot be added."""
    a: dict[str, list[str]] = {"Monday": ["Jon"], "Tuesday": ["Alex"]}
    log: dict[str, list[str]] = {'Monday': ['Jon'], 'Tuesday': ['Alex']}

    assert update_attendance(a, "Monday", "Jon") == log


def test_adding_to_already_existing_day_update_attendance() -> None:
    """Testing that adding a name/string to an already existing day just adds to that specific day's list."""
    a: dict[str, list[str]] = {"Monday": ["Jon", "Louie"], "Tuesday": ["Alex"]}
    log: dict[str, list[str]] = {'Monday': ['Jon', 'Louie'], 'Tuesday': ['Alex', 'Pablo']}

    assert update_attendance(a, "Tuesday", "Pablo") == log


def test_adding_new_day_and_names_update_attendance() -> None:
    """Testing that adding a whole new day and names will create a new list within the log."""
    a: dict[str, list[str]] = {"Monday": ["Jon", "Louie"], "Tuesday": ["Alex"]}
    log: dict[str, list[str]] = {'Monday': ['Jon', 'Louie'], 'Tuesday': ['Alex'], 'Wednesday': ['April']}

    assert update_attendance(a, "Wednesday", "April") == log