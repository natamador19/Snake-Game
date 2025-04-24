from turtle import Turtle

ALIGMENT="center"
FONT=("Arial",24,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updateScoreboard()


    def updateScoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)

    def addScore(self):
        self.score+=1
        self.clear()
        self.updateScoreboard()

    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGMENT, font=FONT)
