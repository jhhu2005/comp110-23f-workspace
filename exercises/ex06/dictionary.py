"""EX06 -  Dictionary Functions."""
__author__ = "730664658"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary."""
    inverted: dict[str, str] = {}

    for key in dictionary:  # Iterates through dictionary to switch each key and value.
        val = dictionary[key]
        if val in inverted:  # If value already exists in the inverted dictionary then raise key error.
            raise KeyError("Cannot have more than one of this key!")
        inverted[val] = key  # Inverted.
        
    return inverted


def favorite_color(col: dict[str, str]) -> str:
    """Returns the color that is in the dictonary most frequently."""
    color_track = dict()

    for i in col:  # Iterates through color keys in dictionary and stores each color into the special color_track dictionary.
        x: str = col[i]
        if x not in color_track:  # If this color wasn't found in the dictionary then set its counter to 0.
            color_track[x] = 0
        color_track[x] += 1  # Adds 1 for each instance the color is found in dict.

    most: int = 0
    popular_color: str = ""  # Stores color as the most seen color.

    for i in color_track:  # Iterates through the color_track dictionary to look for the new max, or most seen color.
        val: int = color_track[i]
        if val > most:
            most = val 
            popular_color = i  # Sets the new most popular color.
    
    return popular_color

            
def count(a: list[str]) -> dict[str, int]:
    """Counts number of times a value has appeared in the list."""
    dict1: dict[str, int] = {}
    for i in a:  # Iterates through the list of values.
        if i in dict1:  # If the value is already in the dictionary.
            dict1[i] += 1  # Add to the counter.
        else:
            dict1[i] = 1
    return dict1
    

def alphabetizer(a: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary that each key is a unique letter and each value is a list of words that begin with that letter."""
    dict1: dict[str, list[str]] = {}
    for i in a:  # Iterates through a to look for first unique letter.
        letter: str = i[0].lower()  # Changes first letter to lowercase so can create list of lowercase and uppercase keys.
        if letter not in dict1:  # Empty list if unique letter was not found yet.
            dict1[letter] = []
        dict1[letter].append(i)  # Adds the word to list of its unique first letter.
    return dict1


def update_attendance(a: dict[str, list[str]], d: str, s: str) -> dict[str, list[str]]:
    """Updates the attendance dictionary/log."""
    if d not in a:  # Simply iterates through the existing attendance log, and if the day doesn't exist yet, add to the log based on input of day.
        a[d] = [] 
    if s not in a[d]:
        a[d].append(s)  # Then adds the names of students to that day for attendance.
    return a