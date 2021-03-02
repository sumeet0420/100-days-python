from turtle import Turtle, Screen
import random

t = Turtle()

colors = ["Red","Green","Black","Yellow","Orange","DarkBlue"]
directions = [0,90,1080, 270]
t.speed("fastest")
for _ in range(400):
    t.color(random.choice(colors))
    t.forward(30)
    t.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()