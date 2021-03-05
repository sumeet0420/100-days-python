import time
from turtle import Screen

from day20.scoreboard import ScoreBoard
from day20.snake import Snake
from day20.food import Food

SLEEP_TIME = 0.3
screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")

# Tracer helps to stop animation. On Update it moves
screen.tracer(0)

score_board = ScoreBoard()
snake = Snake()
food = Food()

# Listening the screen
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    time.sleep(SLEEP_TIME)
    screen.update()
    snake.move()

    ##Detecting collision with food
    if snake.head.distance(food) < 15:
        score_board.update_score_board()
        snake.extend_snake()
        food.get_new_location()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280:
        game_is_on=False
        score_board.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()


    ## Detect Collision with tail or any part of snake

screen.exitonclick()