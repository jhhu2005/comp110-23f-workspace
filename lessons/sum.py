"""Summing the elements of a list using different loops."""
__author__ = "730664658"


def w_sum(vals: list[float]) -> float:
    """Returns sum of all elements."""
    current: int = 0
    list_idx: int = 0
    sum: float = 0.0

    if len(vals) == 0:
        return 0.0

    while current < len(vals):
        sum += vals[list_idx]
        current += 1
        list_idx += 1
    return sum 


def f_sum(vals: list[float]) -> float:
    """Returns sum of all elements using for in loop."""
    if len(vals) == 0:
        return 0.0
    
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns sum of all elements using for in range loop."""
    if len(vals) == 0:
        return 0.0
    
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += (vals[idx])
    return sum
        

print(f_range_sum([1.0, 0.9, 1.1]))
