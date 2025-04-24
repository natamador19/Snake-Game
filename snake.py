from turtle import Turtle
INITIAL_POSITIONS=[(0,0),(-20,0),(-40,0)]
class Snake:

   def __init__(self):
       self.segments=[]
       self.createSnake()
       self.head=self.segments[0]



   def move(self):
       for index in range(len(self.segments)-1,0,-1):
           x_cor=self.segments[index-1].xcor()
           y_cor=self.segments[index-1].ycor()
           self.segments[index].goto( x_cor, y_cor)
       self.head.forward(20)


   def createSnake(self):
       for index in INITIAL_POSITIONS:
           self.add_segment(index)


   def Up(self):
       if self.head.heading() != 270:
            self.head.setheading(90)

   def add_segment(self,position):
       snake = Turtle("square")
       snake.color("white")
       snake.penup()
       snake.goto(position)
       self.segments.append(snake)

   def growSnake(self):
       self.add_segment(self.segments[-1].position())


   def Down(self):
       self.head.setheading(270)

   def Left(self):
       self.head.setheading(180)

   def Right(self):
       self.head.setheading(0)
