from turtle import Turtle

## ScoreBoard Properties
DEFAULT_SCORE=0
UPDATE_SCORE_POINT=10
SCORE_BOARD_POSITION=0, 270
SCORE_BOARD_FONT=("Arial", 14, "bold")
SCORE_BOARD_BG="White"
## Gameover Properties
GAME_OVER_FONT=("Arial", 18, "bold")
GAME_OVER="Game Over"
class ScoreBoard(Turtle):

    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score=DEFAULT_SCORE
        self.get_score_board()


    def update_score_board(self):
        self.clear()
        self.score+=UPDATE_SCORE_POINT
        self.get_score_board()

    def get_score_board(self):
        self.color(SCORE_BOARD_BG)
        self.penup()
        self.goto(SCORE_BOARD_POSITION)
        self.hideturtle()
        self.write(f"Score: {self.score}", font=SCORE_BOARD_FONT)

    def game_over(self):
        self.home()
        self.write(GAME_OVER, font=GAME_OVER_FONT)

