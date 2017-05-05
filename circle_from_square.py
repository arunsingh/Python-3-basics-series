# Author@ Arun Singh | arunsingh.in@gmail.com
#
# Solution to UDACITY Course Project: Learning Python
# Copyright (c) Arun Singh | arunsingh.in@gmail.com. All rights reserved.
#
# https://github.com/arunsingh/udacity_courses/pfw_python
#
# Problem stmt: Draw a circle from square using lines and right angles
# and using draw() function, for re-usability component of code
# I will declare diff function and use the loop
#


import turtle as t


def draw_square(arun_s):
    for x in range(1, 5):
        arun_s.forward(100)
        arun_s.right(90)


def draw_art():
    drawpad = t.Screen()
    drawpad.bgcolor("yellow")

    # creating a turtle Saumya  : shape is square, Turtle draws a square
    saumya = t.Turtle()
    saumya.shape("turtle")
    saumya.color("red")
    saumya.speed(2)

    # for loop for creating circle
    for x in range(1, 37):
        draw_square(saumya)
        saumya.right(10)

    # # creating a turtle Rahil : shape is circle, turtle draws circle
    # rahil = t.Turtle()
    # rahil.shape("pentagon")
    # rahil.color("blue")
    # rahil.speed(2)
    # rahil.circle(100)

    # # creating a turtle varsha : shape is triangle, turtle draws triangle
    # varsha = t.Turtle()
    # varsha.shape("arrow")
    # varsha.color("black")
    # varsha.speed(2)
    # varsha.triangle(100)

    drawpad.exitonclick()


if __name__ == '__main__':
    draw_art()
