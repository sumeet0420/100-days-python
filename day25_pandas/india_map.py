import turtle

import pandas

screen = turtle.Screen()
image = 'India-Blank-Map-Outline.gif'
screen.addshape(image)
turtle.shape(image)
turtle.onscreenclick(lambda x, y: print(x, y))
is_game_on = True
correct_answer = 0
states = pandas.read_csv('india_map.csv')
guessed_answers = []
while correct_answer < 2:
    answer_state = screen.textinput(title=f"state name {correct_answer}", prompt="What's the state name").title()
    if answer_state == 'Exit':
        break
    answer_state_row=states[states['state'] == answer_state]
    if len(answer_state_row) and answer_state not in guessed_answers:
        guessed_answers.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(answer_state_row.x),int(answer_state_row.y))
        t.write(answer_state)
        correct_answer += 1
screen.mainloop()