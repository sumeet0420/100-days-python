import turtle as t
import random


t.speed("fastest")
t.colormode(255)

def get_random_rbg_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def draw_spirograph(size_of_gap):
    for _ in range(360//size_of_gap):
        t.color(get_random_rbg_color())
        t.circle(100)
        t.setheading(t.heading()+size_of_gap)

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()