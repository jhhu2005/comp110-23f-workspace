"""My Turtle Project. A night scene, with the moon and stars, and skyscrapers. On Line 110 and 111 I use a for in range loop utilizing randomint to draw the stars in random locations in the nightsky for the above and beyond points. On line 90 I use the circle method for the above and beyond points. In the skyscraper function, I utilize the window function within it to make it less complex for the above and beyond points."""

__author__ = "730664658"

from turtle import Turtle, tracer, update, colormode, done 
from random import randint
colormode(255)


def makesquare(t: Turtle, side: float) -> None:
    """Makes squares."""
    for i in range(4):
       
        t.forward(side)
        t.right(90)


def window(t: Turtle, x: float, y: float) -> None:
    """Creates windows for the skyscraper as basic squares, with also customizable location."""
    t.goto(x, y)
    t.pendown() 
    t.fillcolor("yellow")
    t.begin_fill() 
    makesquare(t, 10.0)
    t.end_fill()
    t.penup()


def skyscraper(t: Turtle, height: float, width: float, x: float, y: float) -> None:
    """Creates a skyscraper that have customizable heights and widths and locations."""
    t.goto(x, y)
    t.pendown()
    t.fillcolor("gray")
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()
    t.penup()
    
    window(t, x + width / 4, y + height / 4)
    window(t, x + width / 1.90, y + height / 4)
    window(t, x + width / 1.25, y + height / 4)

    window(t, x + width / 4, y + height / 2)
    window(t, x + width / 1.90, y + height / 2)
    window(t, x + width / 1.25, y + height / 2)

    window(t, x + width / 4, y + height / 1.25)
    window(t, x + width / 1.90, y + height / 1.25)
    window(t, x + width / 1.25, y + height / 1.25)

    
def star(t: Turtle, x: int, y: int) -> None:
    """Creates stars for the night sky."""
    t.goto(x, y)
    t.color(225, 193, 110)
    t.pendown()
   
    for i in range(5):
        t.forward(10)
        t.right(144)

    t.penup()


def bigstar(t: Turtle, x: int, y: int) -> None:
    """Creates bigger stars for the night sky."""
    t.goto(x, y)
    t.color(225, 193, 110)
    t.pendown()
   
    for i in range(5):
        t.forward(15)
        t.right(144)

    t.penup()


def moon(t: Turtle, x: int, y: int) -> None:
    """Creates a moon."""
    t.up()
    t.goto(x, y)
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(75)
    t.end_fill()


def main() -> None:
    """Building my scene."""
    tracer(0, 0)  # Disables delay in tracing.
    squirt: Turtle = Turtle()
    squirt.penup()
    squirt.fillcolor("black")
    squirt.goto(-400, -400)
    squirt.begin_fill()
    for i in range(4):
        squirt.forward(1200)
        squirt.left(90)
    squirt.end_fill()
    # Creates background of a night sky. 

    for i in range(15):
        """Using randint function here to get stars to be drawn at random places everytime!"""
        star(squirt, randint(-300, 30), randint(100, 300))
        bigstar(squirt, randint(-300, 30), randint(100, 300))

    squirt.penup()

    skyscraper(squirt, 350.0, 55, -250.0, -275.0)

    squirt.left(90)
    skyscraper(squirt, 200.0, 60.0, -195.0, -275.0)

    squirt.left(90)
    skyscraper(squirt, 250.0, 55.0, -135.0, -275.0)

    moon(squirt, 100, 120)

    squirt.hideturtle()
    update()
    done()
    
    
if __name__ == "__main__":
    main()