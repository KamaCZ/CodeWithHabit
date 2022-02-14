# Using Turtle build-in module
# this module can be used to create animations
# documentation: https://docs.python.org/3/library/turtle.html
# realpythonguide: https://realpython.com/beginners-guide-python-turtle/
# "if abs(pos()) < 1:" explanation: https://stackoverflow.com/questions/39578762/drawing-the-turtle-module
# turtle youtube: https://www.youtube.com/watch?v=pRzzNqK94SI


import turtle
from turtle import *
turtle.bgcolor("pink")
color('red', 'yellow')
begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
end_fill()
done()





"""
kamil_turtle = turtle.Turtle()
kamil_turtle.forward(100)
kamil_turtle.right(90)
kamil_turtle.forward(100)
kamil_turtle.right(90)
kamil_turtle.forward(100)
kamil_turtle.right(90)
kamil_turtle.forward(100)

"""
"""
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(400)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
"""