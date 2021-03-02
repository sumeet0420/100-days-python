#from turtle import Turtle, Screen
import turtle
import random
screen = turtle.Screen()
screen.setup(width=800, height=400)
finish_line_turtle = turtle.Turtle()
finish_line_turtle.color("green")
finish_line_turtle.penup()
finish_line_turtle.forward(250)
finish_line_turtle.left(90)
finish_line_turtle.pendown()
finish_line_turtle.forward(1000)
finish_line_turtle.right(180)
finish_line_turtle.forward(2000)
finish_line_turtle.penup()
is_race_on = False
number_of_players = 5
start_positions = [(x*-20) for x in range(number_of_players)]

def get_random_rbg_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

turtle.colormode(255)
turtle_list = []
for i in range(5):
    tim = turtle.Turtle()
    tim.home()
    tim.color(get_random_rbg_color())
    tim.penup()
    tim.goto(x=-250,y=start_positions[i])
    turtle_list.append((tim, i))

is_race_on=True
while is_race_on:
    for turtle_race, turtle_number in turtle_list:
        if turtle_race.xcor() > 250:
            is_race_on=False
        random_distance = random.randint(0,10)
        turtle_race.forward(random_distance)

screen.exitonclick()
