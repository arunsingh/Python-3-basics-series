# Author@ Arun Singh | arunsingh.in@gmail.com
#
# Solution to UDACITY Course Project: Learning Python
# Copyright (c) Arun Singh | arunsingh.in@gmail.com. All rights reserved.
#
# https://github.com/arunsingh/udacity_courses/pfw_python
#
#
# Draw a Turtle star : Turtle can draw intricate shapes using programs
# that repeat simple moves.


from turtle import *


color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
