def value_exists(a: dict[str, int], i: int) -> bool:
    "Returns true ff value exists in dict."
    exists: bool = False

    for elem in a:
        if a[elem] == i:
            exists = True
    return exists



