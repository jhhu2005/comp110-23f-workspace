"""EX04 - Using List Utility Functions!"""
__author__ = "730664658"

def all (intlist: list[int], givenint: int) -> bool:
    intidx: int = 0
    while len(intlist) > intidx and len(intlist) > 0:
        if intlist[intidx] == givenint:
            intidx += 1
        else:
            return False 
    return True

def max (intlist: list[int]) -> int:
    maxint: int = 0
    intidx: int = 0
    if len(intlist) == 0:
        raise ValueError("max() arg is an empty List")
    while len(intlist) > intidx:
        if intlist[intidx] > maxint:
          maxint = intlist[intidx] 
        intidx += 1
    return maxint

def is_equal (intlist1: list[int], intlist2: list[int]) -> bool:
    intlist1idx: int = 0
    intlist2idx: int = 0
    while intlist1idx < len(intlist1) and intlist2idx < len(intlist2):
        if intlist1[intlist1idx] == intlist2[intlist2idx]:
            intlist1idx += 1
            intlist2idx += 1
        else: 
            return False
    return True

def main():
    result: str = is_equal([1,0,3], [1,2,3])
    print (result)
    
main()