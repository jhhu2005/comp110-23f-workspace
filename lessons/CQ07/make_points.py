"""Calling my point class constructors and methods!"""
from lessons.CQ07.point import Point


my_Point: Point = Point(2.0, 3.0)
print(my_Point.x)
print(my_Point.y)

my_Point.scale_by(2)
print(my_Point.x)
print(my_Point.y)

my_other_Point: Point = my_Point.scale(3)
print(my_other_Point.x)
print(my_other_Point.y)