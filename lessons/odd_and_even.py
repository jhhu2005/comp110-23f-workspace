def odd_and_even (a: list[int]) -> list[int]:
    """Find the odd elements with even indexes"""
    i: int = 0
    b: list[int] = []

    while i < len(a):
        if a[i] % 2 == 1 and i % 2 == 0:
            b.append(a[i])
        i += 1
    return b

print(odd_and_even([7,8,10,10,5,12,3,2,11,8]))