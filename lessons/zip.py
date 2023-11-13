"""Combining two lists into a dictionary."""
__author__ = "730664658"


def zip(word_list: list[str], num_list: list[int]) -> dict[str, int]:
    """Combines word_list and num_list into one dictionary."""
    dict1 = {}
    
    if len(word_list) == len(num_list) and len(word_list) != 0 and len(num_list) != 0:
        dict1 = {word_list[i]: num_list[i] for i in range(len(word_list))}
    else: 
        dict1 = {}
    return dict1


print(zip(["Happy", "Tuesday"], [1, 2]))