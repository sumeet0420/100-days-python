from turtle import Screen, Turtle

turtle = Turtle()

def move_forward():
    turtle.forward(50)

def move_backward():
    turtle.backward(50)

def turn_right():
    turtle.right(90)

def turn_left():
    turtle.left(90)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen = Screen()
screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_right, key="a")
screen.onkey(fun=turn_left, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()

