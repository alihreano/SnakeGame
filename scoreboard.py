from turtle import  Turtle
ALIGNMENT="center"
FONT=('Courier', 20, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.clear()
        self.write(f"The score is : {self.score}",align=ALIGNMENT, font=FONT)
    def score_up(self):
        self.score+=1
        self.update_scoreboard()
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER :(",align=ALIGNMENT, font=FONT)
