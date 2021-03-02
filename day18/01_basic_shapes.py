# This is a sample Python script.

from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("red")

##Draw a square
for _ in range(4):
    turtle.forward(50)
    turtle.right(90)

##Triangle
for _ in range(3):
    turtle.forward(50)
    turtle.right(90)
    turtle.right(30)

turtle.up()
turtle.forward(100)

##Dashed Line
for _ in range(10):
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
turtle.pendown()

turtle.color("Blue")
def draw_shape(num_side):
    angle = 360/num_side
    for _ in range(num_side):
        turtle.forward(100)
        turtle.right(angle)

for side in range(3,11):
    draw_shape(side)

screen = Screen()
screen.exitonclick()