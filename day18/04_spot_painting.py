import colorgram
import random
from turtle import Turtle, Screen
import turtle as t

def extract_colors_from_image():
    colors = colorgram.extract('spot_painting.jpg', 20)
    rgb_colors = [(color.rgb.r,color.rgb.g,color.rgb.b) for color in colors]
    return rgb_colors

#HardCoded Values after extracting values from painting..
rgb_colors = ((229, 225, 221), (218, 229, 220), (233, 220, 226), (218, 223, 230), (230, 207, 91), (225, 149, 91), (122, 167, 187), (35, 110, 158), (163, 13, 22), (127, 177, 145), (233, 81, 49), (202, 67, 27), (192, 186, 23), (174, 18, 13), (33, 129, 49), (7, 99, 37), (13, 64, 39), (12, 41, 76), (242, 203, 4), (139, 79, 92))

turtle = Turtle()
turtle.speed("fastest")
turtle.hideturtle()
turtle.penup()
t.colormode(255)

##Setting Initial Position
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots=100

for dot_count in range(1, number_of_dots+1):
    turtle.dot(20, random.choice(rgb_colors))
    turtle.forward(50)

    if dot_count % 10 ==0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

screen = Screen()
screen.exitonclick()