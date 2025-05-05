from turtle import Turtle

ALIGMENT="center"
FONT=("Arial",24,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score=0
        self.readFile()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updateScoreboard()


    def updateScoreboard(self):
        self.clear()
        self.readFile()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)


    def reset(self):
        if int(self.score)>int(self.high_score):
            self.high_score=self.score
        self.write_new_highscore()
        self.score=0
        self.updateScoreboard()

    def addScore(self):
        self.score+=1
        self.clear()
        self.updateScoreboard()

    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGMENT, font=FONT)

    def readFile(self):
        with open("data.txt", mode="r") as data:
            self.high_score=int(data.read())

    def write_new_highscore(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))


