author = "730664658"


def short_words(a: list[str]) -> list[str]:
    """Filters out shorter words."""
    i: int = 0
    b: list[str] = []

    while i < len(a):
        if len(a[i]) < 5:
            b.append(a[i])
        else:
            print(f"{a[i]} was too long!")
         
        i += 1
        
    return b


print(short_words(["sun", "cloud", "sky"]))