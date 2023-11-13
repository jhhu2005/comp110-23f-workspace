"""EX04 - Using List Utility Functions!"""
__author__ = "730664658"


def all(intlist: list[int], givenint: int) -> bool:
    """Looks for all the same int in list."""
    intidx: int = 0
    if len(intlist) == 0:
        return False
    while len(intlist) > intidx and len(intlist) > 0:
        if intlist[intidx] == givenint:
            intidx += 1
        else:
            return False 
    return True


def max(intlist: list[int]) -> int:
    """Looks for the largest int in list."""
    maxint: int = intlist[0]
    intidx: int = 0
    if len(intlist) == 0:
        raise ValueError("max() arg is an empty List")
    while len(intlist) > intidx:
        if intlist[intidx] > maxint:
            maxint = intlist[intidx] 
        intidx += 1
    return maxint


def is_equal(intlist1: list[int], intlist2: list[int]) -> bool:
    """Looks for two lists of ints to be the same in every index."""
    idx: int = 0
    if len(intlist1) != len(intlist2):
        return False

    while idx < len(intlist1):
        if intlist1[idx] != intlist2[idx]:
            return False
        idx += 1
    return True


print(max([-3, -1, -5]))