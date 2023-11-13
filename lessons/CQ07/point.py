"""Defining the point class! CQ07."""
from __future__ import annotations

__author__ = "730664658"


class Point:
    """My Point Class."""

    x: float
    y: float

    def __init__(self, inp_x_init: float = 0.0, inp_y_init: float = 0.0):
        """Constructor for a Point."""
        self.x = inp_x_init
        self.y = inp_y_init

    def __str__(self):
        """Returns string."""
        output: str = (f"x: {self.x}; y: {self.y}")
        return output

    def scale_by(self, factor: int) -> None:
        """Multiplies x and y by a factor."""
        self.x *= factor
        self.y *= factor 

    def scale(self, factor: int) -> Point:
        """Creates a new point with a factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplication operator overload."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, add: int | float) -> Point:
        """Addition operator overload."""
        new_point: Point = Point(self.x + add, self.y + add)
        return new_point
    

my_point: Point = Point(1.0, 2.0)
new_point: Point = my_point * 3
print(new_point)